# ============================================================
# TUYUL FX AGI v5.7.8 - Reflective VDD Feature Engine
# ------------------------------------------------------------
# Engine reflektif untuk menghitung fitur volatilitas global:
# - Relative Volatility Index (RVI)
# - Fear-Greed Index
# - Term Structure Gradient (VIX contango/backwardation)
#
# Hasil dikirim ke Kartel Repo dan digunakan oleh:
# - VDD Regime Model (vdd_regime_reflective.py)
# - Hybrid Balance Engine
# - BOT-TJX Reflective Bridge
# ============================================================

import json
import math
from datetime import datetime
from statistics import mean
from typing import Dict, List

# ============================================================
# Configurable parameters
# ============================================================

RVI_LOOKBACK = 14
FG_NEUTRAL = 50
TERM_NORMAL = "Contango"


# ============================================================
# RVI calculation
# ============================================================

def calculate_rvi(close_prices: List[float]) -> float:
    """Hitung Relative Volatility Index (RVI)."""
    if len(close_prices) < RVI_LOOKBACK:
        raise ValueError("Data harga terlalu sedikit untuk menghitung RVI.")

    up_vol: List[float] = []
    down_vol: List[float] = []

    for i in range(1, len(close_prices)):
        change = close_prices[i] - close_prices[i - 1]
        if change > 0:
            up_vol.append(abs(change))
            down_vol.append(0.0)
        else:
            down_vol.append(abs(change))
            up_vol.append(0.0)

    avg_up = mean(up_vol[-RVI_LOOKBACK:])
    avg_down = mean(down_vol[-RVI_LOOKBACK:])
    rvi_raw = 100 * (avg_up / (avg_up + avg_down)) if (avg_up + avg_down) > 0 else 50
    return round(rvi_raw / 100, 3)


# ============================================================
# Fear-Greed Index
# ============================================================

def calculate_fear_greed_index(vix: float, spx_change: float, dxy_change: float) -> int:
    """Kalkulasi indeks Fear-Greed berbasis VIX dan aset global."""
    base = FG_NEUTRAL
    vix_adj = (20 - vix) * 1.8
    spx_adj = spx_change * 500
    dxy_adj = -dxy_change * 300

    index = max(0, min(100, base + vix_adj + spx_adj + dxy_adj))
    return int(index)


# ============================================================
# Term structure gradient
# ============================================================

def calculate_term_structure(vix_near: float, vix_far: float) -> str:
    """Menentukan bentuk kurva VIX (Contango/Backwardation)."""
    gradient = vix_far - vix_near
    if gradient > 0.3:
        return "Contango"
    if gradient < -0.3:
        return "Backwardation"
    return "Flat"


# ============================================================
# Reflective feature aggregator
# ============================================================

def generate_reflective_features(
    close_prices: List[float],
    vix: float,
    spx_change: float,
    dxy_change: float,
    vix_near: float,
    vix_far: float,
) -> Dict[str, object]:
    """Gabungkan semua fitur reflektif VDD ke dalam satu paket JSON."""
    rvi = calculate_rvi(close_prices)
    fg_index = calculate_fear_greed_index(vix, spx_change, dxy_change)
    term = calculate_term_structure(vix_near, vix_far)

    result = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "vix_level": vix,
        "rvi": rvi,
        "fear_greed_index": fg_index,
        "term_structure": term,
        "reflective_bridge": "RBP_v2.2",
        "bot": "TUYULBOT-TJX",
    }

    print(f"[VDD Features] RVI={rvi} | Fear-Greed={fg_index} | Term={term}")
    return result


# ============================================================
# Save features to Journal Repo
# ============================================================

def save_reflective_features(data: Dict[str, object], path: str = "journal_repo/vdd_features.json") -> None:
    """Simpan hasil kalkulasi reflektif ke Journal Repo."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"VDD Reflective Features saved -> {path}")


# ============================================================
# Demo eksekusi (untuk BOT-TJX atau manual run)
# ============================================================

if __name__ == "__main__":
    print("Running Reflective VDD Feature Engine v5.7.8...")

    sample_close_prices = [
        12.1,
        12.3,
        12.5,
        12.8,
        12.7,
        12.9,
        13.0,
        13.2,
        13.3,
        13.1,
        12.9,
        13.0,
        13.2,
        13.4,
        13.3,
    ]

    sample_vix = 17.4
    sample_spx_change = 0.0021
    sample_dxy_change = -0.0015
    vix_near, vix_far = 17.2, 17.7

    features = generate_reflective_features(
        sample_close_prices,
        sample_vix,
        sample_spx_change,
        sample_dxy_change,
        vix_near,
        vix_far,
    )

    save_reflective_features(features)
