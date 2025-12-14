# ============================================================
# 🧠 TUYUL FX AGI Hybrid Reflective Engine
# TRQ–M15 Pre-Move v5.8r+++ (Dual Polarity + Monte Carlo)
# ------------------------------------------------------------
# Mendeteksi pre-move reflektif 1–6 jam (Bullish & Bearish)
# + simulasi probabilitas arah via Monte Carlo Polarized R³D
# ============================================================

import json
import os
import time
from datetime import datetime

import numpy as np
import pandas as pd
import requests

# ============================================================
# ⚙️ PARAMETER SISTEM
# ============================================================
PAIR = "AUD/USD"
INTERVAL = "15min"
API_URL = "http://localhost:8000/bridge/fetchLiveData"
ALPHA = 0.52
BETA = 0.31
GAMMA = 0.17
POLARITY_FACTOR = 1.25
PREMOVE_THRESHOLD = 0.9
JOURNAL_PATH = "journal_repo/journal_trq_premove_realtime.json"


# ============================================================
# 🧩 REFLECTIVE ENERGY + POLARITY
# ============================================================
def compute_reflective_energy(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["price_momentum"] = df["close"].diff() / df["close"].shift(1)
    df["price_momentum"].fillna(0, inplace=True)
    df["time_persistence"] = df["close"].rolling(20).apply(lambda x: len(x) / len(df))
    df["depth_imbalance"] = abs(df["buy_vol"] - df["sell_vol"]) / (
        df["buy_vol"] + df["sell_vol"] + 1e-9
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


# ============================================================
# 🧮 MONTE CARLO DUAL POLARITY SIMULATION
# ============================================================
def monte_carlo_reflective(df: pd.DataFrame, iterations: int = 20000) -> dict:
    df = df.copy()
    df["momentum_sign"] = np.sign(df["close"].diff())
    df["R3D_polar"] = df["R3D"] * df["momentum_sign"]

    returns = []
    for _ in range(iterations):
        sample = df["R3D_polar"].sample(frac=1, replace=True).cumsum()
        returns.append(sample.iloc[-1])

    mean = np.mean(returns)
    std = np.std(returns)
    prob_bull = np.sum(np.array(returns) > 0) / iterations
    prob_bear = np.sum(np.array(returns) < 0) / iterations

    return {
        "mean": round(mean, 5),
        "std": round(std, 5),
        "prob_bullish": round(prob_bull * 100, 2),
        "prob_bearish": round(prob_bear * 100, 2),
        "confidence_interval": round(1 - (std / (abs(mean) + 1e-9)), 3),
    }


# ============================================================
# 🧠 DETEKSI PRE-MOVE (DUAL POLARITY)
# ============================================================
def detect_premove(df: pd.DataFrame) -> dict:
    last = df.iloc[-1]
    grad = last["gradient"]
    avg_grad = df["gradient"].mean()
    std_grad = df["gradient"].std()

    conf12 = round(min(1.0, abs(grad) / (abs(avg_grad) + std_grad + 1e-9)), 3)
    wlwci = round(
        np.clip(np.corrcoef(df["R3D"].tail(20), df["close"].tail(20))[0, 1], -1, 1), 3
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
        "r3d_last": round(last["R3D"], 5),
        "delta_r3d": round(last["ΔR3D"], 5),
        "gradient": round(grad, 5),
        "conf12": conf12,
        "wlwci": wlwci,
        "state": state,
        "lead_time_hours": round(est_hours, 1),
        "alert": conf12 >= PREMOVE_THRESHOLD,
    }


# ============================================================
# 🚀 FETCH DATA REALTIME
# ============================================================
def fetch_data() -> pd.DataFrame | None:
    try:
        res = requests.get(f"{API_URL}?pair={PAIR}&interval={INTERVAL}", timeout=10)
        if res.status_code == 200:
            raw = res.json()
            df = pd.DataFrame(raw["values"]) if "values" in raw else pd.DataFrame()
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
        print(f"⚠️ API Response {res.status_code}")
        return None
    except Exception as e:  # noqa: BLE001
        print(f"❌ Fetch error: {e}")
        return None


# ============================================================
# 🧠 MAIN LOOP
# ============================================================
def run_realtime_premove(interval_minutes: int = 15) -> None:
    print(f"\n🐺 TUYUL FX – TRQ–M15 Dual-Polarity + Monte Carlo v5.8r+++")
    print(f"Monitoring {PAIR} setiap {interval_minutes} menit...\n")

    while True:
        df = fetch_data()
        if df is not None and len(df) > 30:
            df = compute_reflective_energy(df)
            df = compute_reflective_gradient(df)
            result = detect_premove(df)

            # Jalankan Monte Carlo dual-bias
            mc = monte_carlo_reflective(df)
            result["monte_carlo"] = mc

            color = (
                "🟢"
                if "Bullish" in result["state"]
                else "🔴" if "Bearish" in result["state"] else "⚪"
            )
            print(
                f"[{result['timestamp']}] {PAIR} {color} {result['state']} | ΔR₃D={result['delta_r3d']} | "
                f"CONF₁₂={result['conf12']} | Lead={result['lead_time_hours']}h"
            )
            print(
                f"🎲 Monte Carlo → Bullish={mc['prob_bullish']}% | Bearish={mc['prob_bearish']}% | CI={mc['confidence_interval']}"
            )

            # Journal update
            os.makedirs(os.path.dirname(JOURNAL_PATH), exist_ok=True)
            with open(JOURNAL_PATH, "a") as f:
                json.dump(result, f)
                f.write("\n")

            # Alerts
            if result["alert"]:
                if "Bullish" in result["state"]:
                    print(
                        f"⚡🐺 PRE-MOVE ALERT → Potensi BREAKOUT BUY ({result['lead_time_hours']} jam)."
                    )
                elif "Bearish" in result["state"]:
                    print(
                        f"⚠️🐺 PRE-MOVE ALERT → Potensi DUMP SELL ({result['lead_time_hours']} jam)."
                    )
        else:
            print("⏳ Waiting for sufficient data...")

        time.sleep(interval_minutes * 60)


# ============================================================
if __name__ == "__main__":
    run_realtime_premove()
