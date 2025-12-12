"""
🧠 Reflective Analyzer – TUYUL FX AGI HYBRID
-----------------------------------------
Analisis Layer–12 menggunakan data real-time:
Reflex → Fusion → Monte → VIX
-----------------------------------------
"""

from datetime import datetime
from core.reflective.reflective_live_bridge import get_fusion_data, fetch_vix_status

def analyze_reflective_layers(pair: str, timeframe: str):
    print(f"🧩 Analisa reflektif real-time untuk {pair} [{timeframe}] ...")

    fusion = get_fusion_data(pair, timeframe)
    vix = fetch_vix_status()

    conf12 = fusion.get("conf12", 0.0)
    wlwci = fusion.get("wlwci", 0.0)
    rcadj = fusion.get("rcadj", 1.0)
    integrity = fusion.get("integrity_index", 0.0)
    bias = fusion.get("bias", "Unknown")

    return {
        "pair": pair,
        "timeframe": timeframe,
        "bias": bias,
        "conf12": conf12,
        "wlwci": wlwci,
        "rcadj": rcadj,
        "integrity": integrity,
        "vix_level": vix.get("vix_level"),
        "global_regime": vix.get("global_regime"),
        "timestamp": datetime.utcnow().isoformat()
    }
