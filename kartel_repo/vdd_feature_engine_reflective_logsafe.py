# ============================================================
# TUYUL FX AGI v5.7.8 - Reflective VDD Feature Engine (LogSafe)
# ------------------------------------------------------------
# Versi reflektif aman dengan integrasi logging BOT-TJX dan Hybrid Balance.
# ============================================================

import json
import os
from datetime import datetime
from statistics import mean
from typing import Dict, List

# ============================================================
# Parameter konfigurasi
# ============================================================

RVI_LOOKBACK = 14
FG_NEUTRAL = 50
LOG_PATH = "logs/vdd_reflective.log"
OUTPUT_PATH = "journal_repo/vdd_features_safe.json"


# ============================================================
# RVI calculation
# ============================================================

def calculate_rvi(close_prices: List[float]) -> float:
    """Hitung Relative Volatility Index (RVI) dengan aman."""
    if len(close_prices) < RVI_LOOKBACK:
        raise ValueError("Data harga terlalu sedikit untuk menghitung RVI.")

    up_vol: List[float] = []
    down_vol: List[float] = []

    for i in range(1, len(close_prices)):
        change = close_prices[i] - close_prices[i - 1]
        up_vol.append(max(change, 0.0))
        down_vol.append(max(-change, 0.0))

    avg_up = mean(up_vol[-RVI_LOOKBACK:])
    avg_down = mean(down_vol[-RVI_LOOKBACK:])
    if avg_up + avg_down == 0:
        return 0.5

    rvi = avg_up / (avg_up + avg_down)
    return round(rvi, 3)


# ============================================================
# Fear-Greed Index
# ============================================================

def calculate_fear_greed_index(vix: float, spx_change: float, dxy_change: float) -> int:
    """Kalkulasi indeks Fear-Greed berbasis volatilitas dan indeks global."""
    base = FG_NEUTRAL
    vix_adj = (20 - vix) * 1.8
    spx_adj = spx_change * 500
    dxy_adj = -dxy_change * 300
    index = base + vix_adj + spx_adj + dxy_adj
    return int(max(0, min(100, index)))


# ============================================================
# Term structure
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
# Reflective feature generator
# ============================================================

def generate_reflective_features(
    close_prices: List[float],
    vix: float,
    spx_change: float,
    dxy_change: float,
    vix_near: float,
    vix_far: float,
) -> Dict[str, str | float | int]:
    """Gabungkan semua fitur reflektif ke dalam satu JSON."""
    rvi = calculate_rvi(close_prices)
    fg_index = calculate_fear_greed_index(vix, spx_change, dxy_change)
    term = calculate_term_structure(vix_near, vix_far)

    data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "vix_level": vix,
        "rvi": rvi,
        "fear_greed_index": fg_index,
        "term_structure": term,
        "reflective_bridge": "RBP_v2.2",
        "bot": "TUYULBOT-TJX",
    }

    log_line = (
        f"[{data['timestamp']}] [VDD Features] "
        f"RVI={rvi:.3f} | Fear-Greed={fg_index} | Term={term} | BOT={data['bot']}"
    )

    _write_log(log_line)
    print(log_line)
    return data


# ============================================================
# File handlers (log + output)
# ============================================================

def _write_log(line: str) -> None:
    """Menulis baris log ke file log reflektif."""
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(line + "\n")


def save_reflective_features(data: Dict[str, str | float | int], path: str = OUTPUT_PATH) -> None:
    """Simpan hasil reflektif ke Journal Repo."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"VDD Reflective Features saved -> {path}")


# ============================================================
# Demo eksekusi
# ============================================================

if __name__ == "__main__":
    print("Running Reflective VDD Feature Engine v5.7.8 (LogSafe)...")

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

    data = generate_reflective_features(
        sample_close_prices,
        sample_vix,
        sample_spx_change,
        sample_dxy_change,
        vix_near,
        vix_far,
    )

    save_reflective_features(data)
