"""TRQ–M15 Multi-Asset Reflective Engine v5.9r++.

Memantau multi-pair FX/komoditas/crypto dan hanya menyimpan sinyal
berprobabilitas ≥90% ke Journal Vault.
"""
from __future__ import annotations

import asyncio
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
import requests

from clients import JournalVaultClient

WATCHLIST: List[str] = [
    "EUR/USD",
    "USD/JPY",
    "GBP/USD",
    "USD/CHF",
    "USD/CAD",
    "AUD/USD",
    "NZD/USD",
    "XAU/USD",
    "XAG/USD",
    "WTI/USD",
    "BTC/USD",
    "ETH/USD",
    "NAS100/USD",
    "SPX500/USD",
]
INTERVAL = "15min"
API_URL = "http://localhost:8000/bridge/fetchLiveData"
ALPHA = 0.52
BETA = 0.31
GAMMA = 0.17
POLARITY_FACTOR = 1.25
PREMOVE_THRESHOLD = 0.9
ITERATIONS = 20000
BASE_DIR = Path(__file__).resolve().parents[2]
JOURNAL_PATH = BASE_DIR / "journal_repo/journal_trq_premove_multi.json"
JOURNAL_ENDPOINT = os.getenv("JOURNAL_VAULT_ENDPOINT", "http://localhost:8000/journal")
JOURNAL_TOKEN = os.getenv("JOURNAL_VAULT_TOKEN", "securetoken")


def compute_reflective_energy(df: pd.DataFrame) -> pd.DataFrame:
    """Hitung energi reflektif R₃D dan komponen pendukung."""
    frame = df.copy()
    frame["price_momentum"] = frame["close"].diff() / frame["close"].shift(1)
    frame["price_momentum"].fillna(0.0, inplace=True)
    frame["time_persistence"] = frame["close"].rolling(20).apply(
        lambda series: len(series) / len(frame)
    )
    frame["depth_imbalance"] = (
        (frame["buy_vol"] - frame["sell_vol"]).abs()
        / (frame["buy_vol"] + frame["sell_vol"] + 1e-9)
    )
    frame["R3D"] = (
        (ALPHA * frame["volume"])
        + (BETA * frame["time_persistence"])
        + (GAMMA * frame["depth_imbalance"])
    ) * (1 + POLARITY_FACTOR * frame["price_momentum"])
    return frame


def compute_reflective_gradient(df: pd.DataFrame) -> pd.DataFrame:
    """Hitung ΔR₃D dan gradien reflektif 5-candle."""
    df["ΔR3D"] = df["R3D"].diff()
    df["gradient"] = df["ΔR3D"].rolling(5).mean()
    return df


def monte_carlo_reflective(df: pd.DataFrame, iterations: int = ITERATIONS) -> Dict[str, float]:
    """Monte Carlo polarisasi R₃D untuk estimasi probabilitas."""
    frame = df.copy()
    frame["momentum_sign"] = np.sign(frame["close"].diff())
    frame["R3D_polar"] = frame["R3D"] * frame["momentum_sign"]

    returns: List[float] = []
    for _ in range(iterations):
        sample = frame["R3D_polar"].sample(frac=1, replace=True).cumsum()
        returns.append(float(sample.iloc[-1]))

    mean = float(np.mean(returns))
    std = float(np.std(returns))
    prob_bullish = float(np.sum(np.array(returns) > 0) / iterations * 100)
    prob_bearish = float(np.sum(np.array(returns) < 0) / iterations * 100)
    confidence_interval = 1 - (std / (abs(mean) + 1e-9))

    return {
        "mean": round(mean, 5),
        "std": round(std, 5),
        "prob_bullish": round(prob_bullish, 2),
        "prob_bearish": round(prob_bearish, 2),
        "confidence_interval": round(confidence_interval, 3),
    }


def detect_premove(df: pd.DataFrame, pair: str) -> Dict[str, object]:
    """Deteksi sinyal pre-move berbasis gradien reflektif."""
    last = df.iloc[-1]
    grad = float(last["gradient"])
    avg_grad = float(df["gradient"].mean())
    std_grad = float(df["gradient"].std())

    conf12 = round(min(1.0, abs(grad) / (abs(avg_grad) + std_grad + 1e-9)), 3)

    r3d_tail = df["R3D"].tail(20).values
    price_tail = df["close"].tail(20).values
    mask = ~(np.isnan(r3d_tail) | np.isnan(price_tail))
    if mask.sum() >= 2:
        wlwci = float(np.clip(np.corrcoef(r3d_tail[mask], price_tail[mask])[0, 1], -1, 1))
    else:
        wlwci = 0.0
    wlwci = round(wlwci if not np.isnan(wlwci) else 0.0, 3)

    if grad > 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bullish Pre-Move"
    elif grad < 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bearish Pre-Move"
    else:
        state = "Neutral"

    est_hours = 1 + (6 * conf12) if conf12 >= PREMOVE_THRESHOLD else 0.0

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "pair": pair,
        "r3d_last": round(float(last["R3D"]), 5),
        "delta_r3d": round(float(last["ΔR3D"]), 5),
        "gradient": round(grad, 5),
        "conf12": conf12,
        "wlwci": wlwci,
        "state": state,
        "lead_time_hours": round(est_hours, 1),
        "alert": conf12 >= PREMOVE_THRESHOLD,
    }


def fetch_data(pair: str) -> Optional[pd.DataFrame]:
    """Ambil data live M15 untuk pair tertentu."""
    try:
        response = requests.get(f"{API_URL}?pair={pair}&interval={INTERVAL}", timeout=10)
        if response.status_code != 200:
            print(f"❌ {pair} fetch error: status {response.status_code}")
            return None

        payload = response.json()
        values = payload.get("values", [])
        if not values:
            return None

        frame = pd.DataFrame(values)
        frame = frame.rename(columns={"datetime": "time"})
        frame["close"] = frame["close"].astype(float)
        frame["volume"] = frame["volume"].astype(float)
        frame["buy_vol"] = frame["volume"] * np.random.uniform(0.45, 0.55, len(frame))
        frame["sell_vol"] = frame["volume"] - frame["buy_vol"]
        return frame.sort_values("time")
    except Exception as exc:  # noqa: BLE001
        print(f"❌ {pair} fetch exception: {exc}")
    return None


def append_journal(record: Dict[str, object], journal_path: Path = JOURNAL_PATH) -> None:
    """Tambahkan record ke journal JSONL multi-pair."""
    journal_path.parent.mkdir(parents=True, exist_ok=True)
    with journal_path.open("a", encoding="utf-8") as handler:
        handler.write(json.dumps(record))
        handler.write("\n")


async def _sync_reflective_log(vault: JournalVaultClient, payload: Dict[str, object]) -> None:
    await vault.write_reflective_log(payload)


def run_multi_premove(interval_minutes: int = 15) -> None:
    """Jalankan loop reflektif multi-pair dengan filter probabilitas 90%."""
    print("\n🐺 TUYUL FX – TRQ–M15 Multi-Asset Engine v5.9r++ (Strict ≥90%)")
    print(f"Total pair aktif: {len(WATCHLIST)}\n")

    vault = JournalVaultClient(JOURNAL_ENDPOINT, JOURNAL_TOKEN)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        while True:
            for pair in WATCHLIST:
                df = fetch_data(pair)
                if df is None or len(df) <= 30:
                    print(f"⏳ {pair} data belum cukup.")
                    continue

                df = compute_reflective_energy(df)
                df = compute_reflective_gradient(df)
                result = detect_premove(df, pair)
                monte_carlo = monte_carlo_reflective(df)
                result["monte_carlo"] = monte_carlo

                if not result["alert"]:
                    continue

                max_prob = max(monte_carlo["prob_bullish"], monte_carlo["prob_bearish"])
                if max_prob < 90.0:
                    print(
                        f"🚫 {pair} → Probabilitas <90% "
                        f"(Bull={monte_carlo['prob_bullish']}% / "
                        f"Bear={monte_carlo['prob_bearish']}%)"
                    )
                    continue

                result.update(
                    {
                        "fusion_state": "Stable",
                        "integrity_index": monte_carlo["confidence_interval"],
                        "reflective_sync": "Online",
                        "bias": "Bullish"
                        if monte_carlo["prob_bullish"] > monte_carlo["prob_bearish"]
                        else "Bearish",
                    }
                )

                append_journal(result)
                loop.run_until_complete(_sync_reflective_log(vault, result))
                print(
                    f"✅ {pair} | {result['bias']} {max_prob}% | "
                    f"CONF₁₂={result['conf12']} | WLWCI={result['wlwci']}"
                )

            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\n🛑 Multi-asset loop interrupted by user.")
    finally:
        loop.run_until_complete(vault.aclose())
        loop.close()


if __name__ == "__main__":
    run_multi_premove()
