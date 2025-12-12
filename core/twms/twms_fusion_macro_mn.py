# ============================================================
# 🧠 TUYUL FX AGI v5.8.2-HYBRID
# TWMS Fusion Macro MN (Monthly Macro Trend Layer)
# + FTA (Fundamental Trend Alignment) Integration
# ============================================================

import numpy as np
import pandas as pd
from typing import Dict, Any

# ============================================================
# 🔹 CONFIG
# ============================================================
EMA_PERIOD = 50
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
WINDOW = 20  # untuk regresi slope TWMS
FTA_WEIGHT = 0.25  # bobot fundamental alignment dalam final fusion

# ============================================================
# 🔹 CORE FUNCTIONS
# ============================================================

def calculate_twms_slope(prices: np.ndarray) -> float:
    """Hitung slope tren (wave motion) dengan regresi linear + normalisasi ATR"""
    x = np.arange(len(prices))
    coeffs = np.polyfit(x, prices, 1)
    slope = coeffs[0]
    atr = np.mean(np.abs(np.diff(prices))) or 1e-6
    normalized_slope = float(np.clip(slope / atr, -1.0, 1.0))
    return normalized_slope


def calculate_macd(prices: np.ndarray) -> Dict[str, float]:
    """Hitung MACD dan histogram"""
    ema_fast = pd.Series(prices).ewm(span=MACD_FAST, adjust=False).mean()
    ema_slow = pd.Series(prices).ewm(span=MACD_SLOW, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal = macd_line.ewm(span=MACD_SIGNAL, adjust=False).mean()
    hist = macd_line - signal
    return {"macd": macd_line.iloc[-1], "signal": signal.iloc[-1], "hist": hist.iloc[-1]}


def calculate_ema_strength(prices: np.ndarray) -> float:
    """Validasi kekuatan tren berdasarkan jarak harga terhadap EMA"""
    ema = pd.Series(prices).ewm(span=EMA_PERIOD, adjust=False).mean()
    distance = abs(prices[-1] - ema.iloc[-1]) / np.mean(prices)
    strength = float(np.clip(distance * 10, 0.0, 1.0))
    return strength


def detect_monthly_pattern(data: pd.DataFrame) -> str:
    """
    Deteksi pola makro bulanan:
    - impulsive (tren kuat)
    - corrective (retracement)
    - transitional (reversal early)
    """
    slope = calculate_twms_slope(data["close"].values)
    ema_strength = calculate_ema_strength(data["close"].values)
    if slope > 0.5 and ema_strength > 0.7:
        return "impulsive"
    elif abs(slope) < 0.2:
        return "corrective"
    else:
        return "transitional"


# ============================================================
# 🔹 FTA FUNDAMENTAL ALIGNMENT
# ============================================================

def fta_alignment(fundamental_bias: str, inflation_trend: float, rate_diff: float) -> float:
    """
    FTA = Fundamental Trend Alignment
    Evaluasi kesesuaian tren makro ekonomi dengan arah teknikal TWMS.
    Return score 0–1 (semakin tinggi = semakin align)
    """
    score = 0.5

    # Pengaruh inflasi (proksi kekuatan ekonomi)
    if inflation_trend > 0:
        score += 0.1
    else:
        score -= 0.1

    # Perbedaan suku bunga antarnegara (spread rate differential)
    score += np.clip(rate_diff / 5, -0.2, 0.2)

    # Bias fundamental utama
    if fundamental_bias.lower() in ["bullish", "hawkish", "expansion"]:
        score += 0.2
    elif fundamental_bias.lower() in ["bearish", "dovish", "contraction"]:
        score -= 0.2

    return float(np.clip(score, 0.0, 1.0))


# ============================================================
# 🔹 TWMS FUSION MACRO MN (MAIN FUNCTION)
# ============================================================

def twms_fusion_macro_mn(data: pd.DataFrame, fundamentals: Dict[str, Any]) -> Dict[str, Any]:
    """
    Jalankan analisis TWMS Macro Monthly:
    Menggabungkan slope + momentum + EMA + FTA fundamental alignment
    """
    closes = data["close"].values[-WINDOW:]

    # 1️⃣ Slope (TWMS)
    slope = calculate_twms_slope(closes)

    # 2️⃣ MACD Fusion
    macd_data = calculate_macd(closes)
    tmfi = (slope * 0.5) + (macd_data["hist"] * 0.5)
    tmfi = float(np.clip(tmfi, -1.0, 1.0))

    # 3️⃣ EMA Strength
    ema_strength = calculate_ema_strength(closes)

    # 4️⃣ Monthly Pattern
    pattern = detect_monthly_pattern(data)

    # 5️⃣ FTA Alignment
    fta_score = fta_alignment(
        fundamentals.get("bias", "neutral"),
        fundamentals.get("inflation_trend", 0.0),
        fundamentals.get("rate_diff", 0.0),
    )

    # 6️⃣ Fusion Integration
    fusion_confidence = np.clip(
        (abs(slope) * 0.35)
        + (ema_strength * 0.25)
        + (fta_score * FTA_WEIGHT)
        + (abs(tmfi) * 0.15),
        0.0,
        1.0,
    )

    # 7️⃣ Final Bias
    bias = "Bullish" if tmfi > 0.2 else "Bearish" if tmfi < -0.2 else "Neutral"

    return {
        "TWMS_Slope": round(slope, 3),
        "TMFI": round(tmfi, 3),
        "EMA_Strength": round(ema_strength, 3),
        "FTA_Score": round(fta_score, 3),
        "Fusion_Confidence": round(float(fusion_confidence), 3),
        "Pattern": pattern,
        "Bias": bias,
    }


# ============================================================
# 🧪 TEST DEMO
# ============================================================
if __name__ == "__main__":
    np.random.seed(42)
    prices = np.cumsum(np.random.randn(100) * 0.5 + 0.1) + 100
    df = pd.DataFrame({"close": prices})

    fundamentals = {
        "bias": "bullish",
        "inflation_trend": 0.3,
        "rate_diff": 1.2,
    }

    result = twms_fusion_macro_mn(df, fundamentals)
    print("\n🧠 TWMS Fusion Macro MN (with FTA)")
    for k, v in result.items():
        print(f"{k:15}: {v}")
