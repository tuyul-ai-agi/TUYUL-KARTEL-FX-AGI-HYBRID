"""Reflective adaptive data feed connector for TUYUL FX AGI HYBRID v5.7.3r++.

✅ core/utils/data_feed_adapter.py
Versi v5.7.3r++ — Reflective Adaptive Data Feed Connector

Features:
- Mengambil feed harga & volume (mock / live)
- Menghitung reflective bias awal berdasarkan regime global (VIX, RVI)
- Memberikan awareness tag untuk pipeline reflektif

Pembaruan Reflektif:
- Mode: Mock-only → Adaptive + Live Ready
- Awareness: none → VIX, RVI, Regime awareness
- Reflective bias: baru dengan basis VIX
- Volume adaptif: adjust by global volatility
- Metadata: timestamp, regime, volatility level
- Integrasi: standalone → Quad Repo (Hybrid ← Kartel)
- Output: price + volume → + feed meta JSON

Contoh output:
[Feed] XAUUSD | Regime=Stressed | VIX=27.3 | Bias=0.421
{
  "symbol": "XAUUSD",
  "timestamp": "2025-12-13T15:59:32.921Z",
  "regime": "Stressed",
  "fear_greed": "Fear",
  "vix": 27.3,
  "rvi": 0.38,
  "reflective_bias": 0.421,
  "volatility_level": "High"
}

Integrasi dengan sistem reflektif:
- TWMS (L1): sumber feed dasar → core/twms/twms_scan.py
- Reflex (L3): mikro harga adaptif → core/reflex/reflex_analyzer.py
- Fusion (L10–L12): integrasi ke TRQ3D / CONF₁₂ → core/fusion/fusion_confidence.py
- Reflective Loop: adaptive awareness → core/reflective/reflective_loop_handler.py

“Feed bukan sekadar data — tapi denyut pasar yang disadari.”
“TUYUL membaca bukan hanya harga, tapi niat di balik volatilitas.” ⚡🐺
"""

from typing import Any, Dict, List, Tuple
import datetime
import json
import numpy as np

DEFAULT_MACRO_CONTEXT: Dict[str, Any] = {
    "VIX": 21.8,
    "RVI": 0.4,
    "Regime": "Tranquil",
    "FearGreed": "Neutral",
}


def load_macro_context(path: str = "../kartel_repo/repo/macro_context_cache.json") -> Dict[str, Any]:
    """Ambil konteks makro global untuk mode reflektif (fallback jika tidak ditemukan)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            macro = json.load(f)
        return {
            "VIX": macro.get("VIX", 20.5),
            "RVI": macro.get("RVI", 0.42),
            "Regime": macro.get("GlobalRegime", "Neutral"),
            "FearGreed": macro.get("FearGreed", "Neutral"),
        }
    except FileNotFoundError:
        return DEFAULT_MACRO_CONTEXT


def load_price_volume(
    symbol: str = "EURUSD", n: int = 200, live: bool = False
) -> Tuple[List[float], List[float], Dict[str, Any]]:
    """Memuat data harga dan volume reflektif adaptif."""
    if live:
        raise NotImplementedError("Live feed belum diintegrasikan (tuyul_data_bridge).")

    macro = load_macro_context()
    vix = macro["VIX"]
    regime = macro["Regime"]

    base_price = {
        "EURUSD": 1.10,
        "XAUUSD": 2300,
        "GBPUSD": 1.26,
        "USDJPY": 147.0,
        "BTCUSD": 42000,
    }.get(symbol, 1.10)

    if regime == "Expansion":
        volatility = 0.0025
    elif regime == "Stressed":
        volatility = 0.004
    else:
        volatility = 0.0015

    price = base_price + np.cumsum(np.random.randn(n) * volatility)
    volume = np.random.randint(100, 2000, n)

    bias_factor = np.clip(1 - (vix / 100), 0.5, 1.0)
    adaptive_volume = volume * bias_factor
    reflective_bias = np.tanh((adaptive_volume.mean() / 1000) * (1 - bias_factor))

    feed_meta = {
        "symbol": symbol,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "regime": regime,
        "fear_greed": macro["FearGreed"],
        "vix": vix,
        "rvi": macro["RVI"],
        "reflective_bias": round(float(reflective_bias), 3),
        "volatility_level": "High" if vix > 25 else "Moderate" if vix > 18 else "Calm",
    }

    print(f"[Feed] {symbol} | Regime={regime} | VIX={vix} | Bias={feed_meta['reflective_bias']}")
    return price.tolist(), adaptive_volume.tolist(), feed_meta


if __name__ == "__main__":
    price, vol, meta = load_price_volume("XAUUSD", n=150)
    print(json.dumps(meta, indent=2))
