"""
🧠 TUYUL FX AGI HYBRID – TRQ–M15 v5.9r
Reflective Pre-Move Engine (Dual Polarity + Monte Carlo + Vault Sync)
"""

import asyncio
import json
import os
import time
from datetime import datetime
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
import requests

from clients.journal_vault_client import JournalVaultClient

PAIR = "AUD/USD"
INTERVAL = "15min"
API_URL = "http://localhost:8000/bridge/fetchLiveData"
ALPHA = 0.52
BETA = 0.31
GAMMA = 0.17
POLARITY_FACTOR = 1.25
PREMOVE_THRESHOLD = 0.9
JOURNAL_PATH = "journal_repo/journal_trq_premove_realtime.json"
ITER = 20000


def compute_reflective_energy(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["price_momentum"] = df["close"].diff() / df["close"].shift(1)
    df["price_momentum"].fillna(0, inplace=True)
    df["time_persistence"] = df["close"].rolling(20).apply(lambda x: len(x) / len(df))
    df["depth_imbalance"] = (
        abs(df["buy_vol"] - df["sell_vol"]) / (df["buy_vol"] + df["sell_vol"] + 1e-9)
    )
    df["R3D"] = (
        (ALPHA * df["volume"])
        + (BETA * df["time_persistence"])
        + (GAMMA * df["depth_imbalance"])
    ) * (1 + POLARITY_FACTOR * df["price_momentum"])
    return df


def compute_reflective_gradient(df: pd.DataFrame) -> pd.DataFrame:
    df["ΔR3D"] = df["R3D"].diff()
    df["gradient"] = df["ΔR3D"].rolling(5).mean()
    return df


def monte_carlo_reflective(df: pd.DataFrame, iterations: int = ITER) -> Dict[str, float]:
    df = df.copy()
    df["momentum_sign"] = np.sign(df["close"].diff())
    df["R3D_polar"] = df["R3D"] * df["momentum_sign"]

    returns = []
    for _ in range(iterations):
        sample = df["R3D_polar"].sample(frac=1, replace=True).cumsum()
        returns.append(sample.iloc[-1])

    mean = float(np.mean(returns))
    std = float(np.std(returns))
    prob_bull = float(np.sum(np.array(returns) > 0) / iterations)
    prob_bear = float(np.sum(np.array(returns) < 0) / iterations)

    return {
        "mean": round(mean, 5),
        "std": round(std, 5),
        "prob_bullish": round(prob_bull * 100, 2),
        "prob_bearish": round(prob_bear * 100, 2),
        "confidence_interval": round(1 - (std / (abs(mean) + 1e-9)), 3),
    }


def detect_premove(df: pd.DataFrame) -> Dict[str, Any]:
    last = df.iloc[-1]
    grad = float(last["gradient"])
    avg_grad = float(df["gradient"].mean())
    std_grad = float(df["gradient"].std())

    conf12 = round(min(1.0, abs(grad) / (abs(avg_grad) + std_grad + 1e-9)), 3)
    wlwci = round(
        np.clip(np.corrcoef(df["R3D"].tail(20), df["close"].tail(20))[0, 1], -1, 1),
        3,
    )

    if grad > 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bullish Pre-Move"
    elif grad < 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bearish Pre-Move"
    else:
        state = "Neutral"

    est_hours = 1 + (6 * conf12) if conf12 >= PREMOVE_THRESHOLD else 0
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "pair": PAIR,
        "r3d_last": round(float(last["R3D"]), 5),
        "delta_r3d": round(float(last["ΔR3D"]), 5),
        "gradient": round(grad, 5),
        "conf12": conf12,
        "wlwci": wlwci,
        "state": state,
        "lead_time_hours": round(est_hours, 1),
        "alert": conf12 >= PREMOVE_THRESHOLD,
    }


def fetch_data() -> Optional[pd.DataFrame]:
    try:
        res = requests.get(f"{API_URL}?pair={PAIR}&interval={INTERVAL}", timeout=10)
        if res.status_code == 200:
            raw = res.json()
            df = pd.DataFrame(raw.get("values", []))
            if df.empty:
                return None

            df = df.rename(
                columns={
                    "datetime": "time",
                    "close": "close",
                    "high": "high",
                    "low": "low",
                    "volume": "volume",
                }
            )
            df["close"] = df["close"].astype(float)
            df["volume"] = df["volume"].astype(float)
            df["buy_vol"] = df["volume"] * np.random.uniform(0.45, 0.55, len(df))
            df["sell_vol"] = df["volume"] - df["buy_vol"]
            return df.sort_values("time")
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Fetch error: {exc}")
    return None


def _persist_local_log(payload: Dict[str, Any]) -> None:
    try:
        os.makedirs(os.path.dirname(JOURNAL_PATH), exist_ok=True)
        with open(JOURNAL_PATH, "a", encoding="utf-8") as handle:
            json.dump(payload, handle)
            handle.write("\n")
    except OSError as exc:
        print(f"⚠️ Local journal write failed: {exc}")


def _sync_to_vault(vault: JournalVaultClient, payload: Dict[str, Any]) -> None:
    try:
        asyncio.run(vault.write_reflective_log(payload))
    except Exception as exc:  # noqa: BLE001
        print(f"⚠️ Vault sync failed: {exc}")


def run_realtime_premove(interval_minutes: int = 15) -> None:
    print("\n🐺 TUYUL FX – TRQ–M15 v5.9r (Auto Vault Sync + Strict ≥90%)")
    print(f"Monitoring {PAIR} setiap {interval_minutes} menit...\n")

    vault = JournalVaultClient("http://localhost:8000/journal", token="securetoken")

    while True:
        df = fetch_data()
        if df is not None and len(df) > 30:
            df = compute_reflective_energy(df)
            df = compute_reflective_gradient(df)
            result = detect_premove(df)
            mc = monte_carlo_reflective(df)
            result["monte_carlo"] = mc

            color = (
                "🟢"
                if "Bullish" in result["state"]
                else "🔴" if "Bearish" in result["state"] else "⚪"
            )
            print(
                f"[{result['timestamp']}] {PAIR} {color} {result['state']} | "
                f"ΔR₃D={result['delta_r3d']} | CONF₁₂={result['conf12']} | "
                f"Lead={result['lead_time_hours']}h"
            )
            print(
                "🎲 Monte Carlo → "
                f"Bullish={mc['prob_bullish']}% | "
                f"Bearish={mc['prob_bearish']}% | CI={mc['confidence_interval']}"
            )

            if result["alert"]:
                max_prob = max(mc["prob_bullish"], mc["prob_bearish"])
                if max_prob >= 90.0:
                    result["fusion_state"] = "Stable"
                    result["integrity_index"] = mc["confidence_interval"]
                    result["reflective_sync"] = "Online"

                    print(
                        "✅🐺 VALID REFLECTIVE SIGNAL → "
                        f"{result['state']} ({max_prob}%) | CONF₁₂={result['conf12']}"
                    )
                    _persist_local_log(result)
                    _sync_to_vault(vault, result)
                else:
                    print(f"🚫 Probabilitas <90% → sinyal {result['state']} diabaikan.")
        else:
            print("⏳ Waiting for sufficient data...")

        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    run_realtime_premove()
