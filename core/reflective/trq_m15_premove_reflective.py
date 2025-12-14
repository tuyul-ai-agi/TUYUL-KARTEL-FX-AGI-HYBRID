# ============================================================
# 🧠 TRQ–M15 Pre-Move Reflective Analysis v5.8r
# ------------------------------------------------------------
# TUYUL KARTEL FX – Reflective Discipline Engine
# Mendeteksi energi reflektif 1–6 jam sebelum pergerakan besar.
# ------------------------------------------------------------
# Pipeline: TWMS → EMA → Reflex → TRQ-3D → RGO → REE–FRPC → FusionConf₁₂
# ============================================================

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional
import json
import os

# ============================================================
# ⚙️ PARAMETER SISTEM
# ============================================================
ALPHA = 0.52   # Volume weight
BETA = 0.31    # Time persistence weight
GAMMA = 0.17   # Depth imbalance weight
LEARNING_RATE = 0.01
WINDOW = 96    # 96 x 15min = 24 jam
PREMOVE_THRESHOLD = 0.9

# Path untuk journal output
JOURNAL_PATH = os.path.join(os.path.dirname(__file__), "../../journal_repo/journal_trq_premove.json")

# ============================================================
# 🧩 FUNGSI REFLEKTIF
# ============================================================

def compute_reflective_energy(df: pd.DataFrame) -> pd.DataFrame:
    """
    Hitung Reflective Energy R₃D per candle.
    
    R₃D = α·Volume + β·TimePersistence + γ·DepthImbalance
    
    Args:
        df: DataFrame dengan kolom price, volume, buy_vol, sell_vol
        
    Returns:
        DataFrame dengan kolom R3D ditambahkan
    """
    df = df.copy()
    df["time_persistence"] = df["price"].rolling(20).apply(lambda x: len(x)/len(df))
    df["depth_imbalance"] = abs(df["buy_vol"] - df["sell_vol"]) / (df["buy_vol"] + df["sell_vol"] + 1e-9)
    df["R3D"] = (ALPHA * df["volume"] +
                 BETA * df["time_persistence"] +
                 GAMMA * df["depth_imbalance"])
    return df


def compute_reflective_gradient(df: pd.DataFrame) -> pd.DataFrame:
    """
    Hitung ΔR₃D dan gradien reflektif.
    
    ΔR₃D = R₃D[t] - R₃D[t-1]
    Gradient = SMA(ΔR₃D, 5)
    
    Args:
        df: DataFrame dengan kolom R3D
        
    Returns:
        DataFrame dengan kolom ΔR3D dan gradient ditambahkan
    """
    df["ΔR3D"] = df["R3D"].diff()
    df["gradient"] = df["ΔR3D"].rolling(5).mean()
    return df


def detect_premove(df: pd.DataFrame, pair: str = "AUD/USD") -> dict:
    """
    Deteksi sinyal pre-move 1–6 jam sebelum breakout.
    
    Menghitung:
    - CONF₁₂: Confidence score berdasarkan gradient vs average
    - WLWCI: Weighted Linear Weighted Correlation Index
    - State: Bullish/Bearish Pre-Move atau Neutral
    - Lead Time: Estimasi waktu sebelum breakout (jam)
    
    Args:
        df: DataFrame dengan kolom R3D, ΔR3D, gradient, price
        pair: Currency pair yang dianalisa
        
    Returns:
        Dictionary berisi hasil analisa reflektif
    """
    last = df.iloc[-1]
    grad = last["gradient"]
    avg_grad = df["gradient"].mean()
    std_grad = df["gradient"].std()
    
    # CONF₁₂: Normalized confidence score
    conf12 = round(min(1.0, abs(grad) / (abs(avg_grad) + std_grad + 1e-9)), 3)
    
    # WLWCI: Korelasi antara R3D dan price (20 candle terakhir)
    r3d_tail = df["R3D"].tail(20).values
    price_tail = df["price"].tail(20).values
    
    # Handle NaN values untuk korelasi
    valid_mask = ~(np.isnan(r3d_tail) | np.isnan(price_tail))
    if valid_mask.sum() >= 2:
        wlwci = round(np.clip(np.corrcoef(r3d_tail[valid_mask], price_tail[valid_mask])[0, 1], -1, 1), 3)
    else:
        wlwci = 0.0
    
    # Handle NaN wlwci
    if np.isnan(wlwci):
        wlwci = 0.0

    # Determine state
    if grad > 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bullish Pre-Move"
    elif grad < 0 and conf12 >= PREMOVE_THRESHOLD:
        state = "Bearish Pre-Move"
    else:
        state = "Neutral"

    # Estimated lead time (1-6 jam jika valid)
    est_hours = 1 + (6 * conf12) if conf12 >= PREMOVE_THRESHOLD else 0

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "pair": pair,
        "r3d_last": round(float(last["R3D"]), 4) if not np.isnan(last["R3D"]) else 0.0,
        "delta_r3d": round(float(last["ΔR3D"]), 4) if not np.isnan(last["ΔR3D"]) else 0.0,
        "gradient": round(float(grad), 4) if not np.isnan(grad) else 0.0,
        "conf12": conf12,
        "wlwci": wlwci,
        "state": state,
        "lead_time_hours": round(est_hours, 1),
        "alert": conf12 >= PREMOVE_THRESHOLD
    }


def save_to_journal(result: dict, journal_path: Optional[str] = None) -> bool:
    """
    Simpan hasil analisa ke journal reflektif.
    
    Args:
        result: Dictionary hasil dari detect_premove()
        journal_path: Path ke file journal (optional)
        
    Returns:
        True jika berhasil disimpan
    """
    if journal_path is None:
        journal_path = JOURNAL_PATH
    
    try:
        # Pastikan direktori ada
        os.makedirs(os.path.dirname(journal_path), exist_ok=True)
        
        with open(journal_path, "a") as f:
            json.dump(result, f)
            f.write("\n")
        return True
    except Exception as e:
        print(f"❌ Error saving journal: {e}")
        return False


def run_analysis(df: Optional[pd.DataFrame] = None, pair: str = "AUD/USD", verbose: bool = True) -> dict:
    """
    Jalankan analisa reflektif lengkap.
    
    Args:
        df: Optional DataFrame dengan data M15 (akan generate dummy jika None)
        pair: Currency pair
        verbose: Print hasil ke console
        
    Returns:
        Dictionary hasil analisa
    """
    # Generate dummy data jika tidak ada input
    if df is None:
        np.random.seed(int(datetime.utcnow().timestamp()) % 1000)
        data = {
            "time": pd.date_range(end=datetime.utcnow(), periods=WINDOW, freq="15min"),
            "price": np.linspace(0.6600, 0.6700, WINDOW) + np.random.normal(0, 0.0008, WINDOW),
            "volume": np.random.randint(500, 1500, WINDOW),
            "buy_vol": np.random.randint(200, 800, WINDOW),
            "sell_vol": np.random.randint(200, 800, WINDOW)
        }
        df = pd.DataFrame(data)
    
    # Pipeline analisa
    df = compute_reflective_energy(df)
    df = compute_reflective_gradient(df)
    result = detect_premove(df, pair=pair)
    
    if verbose:
        print_analysis(result)
    
    # Simpan ke journal jika alert valid
    if result["alert"]:
        if save_to_journal(result):
            if verbose:
                print("📜 Journal updated → journal_trq_premove.json")
    
    return result


def print_analysis(result: dict):
    """Print hasil analisa dalam format yang rapi."""
    print("\n🧠 TRQ–M15 Reflective Pre-Move Analysis")
    print("=" * 40)
    print(f"Timestamp        : {result['timestamp']}")
    print(f"Pair             : {result['pair']}")
    print(f"Reflective Energy: {result['r3d_last']}")
    print(f"ΔR₃D             : {result['delta_r3d']}")
    print(f"Gradient         : {result['gradient']}")
    print(f"CONF₁₂           : {result['conf12']}")
    print(f"WLWCI            : {result['wlwci']}")
    print(f"State            : {result['state']}")
    print(f"Lead Time (hrs)  : {result['lead_time_hours']}")
    print(f"Pre-Move Alert   : {'✅ VALID' if result['alert'] else '❌ Not yet'}")


# ============================================================
# 🧪 EKSEKUSI UTAMA
# ============================================================
if __name__ == "__main__":
    result = run_analysis(verbose=True)
