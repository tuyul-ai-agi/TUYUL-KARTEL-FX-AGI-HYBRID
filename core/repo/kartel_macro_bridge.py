# ===============================================================
# 🌍 Kartel Macro Bridge – Integrasi Data Makro Global
# TUYUL FX AGI v5.7.3r++ – Adaptive Reflective Macro Feed
# ===============================================================
# Layer: Fusion Reflective (L11–L12)
# Purpose:
#   Mengambil dan menyelaraskan data makro (VIX, RVI, Regime)
#   dari Kartel Repo untuk integrasi CONF₁₂ dan RCAdj
# ===============================================================

import json
import os
from datetime import datetime
from typing import Any, Dict


def get_macro_context(
    repo_path: str = "../repos/kartel_repo/macro_context_cache.json",
) -> Dict[str, Any]:
    """Ambil data makro reflektif dengan fallback adaptif.

    Args:
        repo_path: Lokasi cache makro dari Kartel Repo.

    Returns:
        Dict berisi VIX, RVI, GlobalRegime, timestamp, dan integrity_index.
    """

    try:
        if not os.path.exists(repo_path):
            raise FileNotFoundError("Macro cache not found")

        with open(repo_path, "r", encoding="utf-8") as file:
            macro = json.load(file)

        vix = float(macro.get("VIX", 22.0))
        rvi = float(macro.get("RVI", 0.45))
        regime = macro.get("GlobalRegime", "Neutral")

        integrity_index = 1.0 if all([vix, rvi, regime]) else 0.85

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "VIX": round(vix, 2),
            "RVI": round(rvi, 3),
            "GlobalRegime": regime,
            "integrity_index": round(integrity_index, 3),
        }

    except Exception as exc:
        fallback = {
            "timestamp": datetime.utcnow().isoformat(),
            "VIX": 24.2,
            "RVI": 0.38,
            "GlobalRegime": "Tranquil",
            "integrity_index": 0.82,
        }
        print(f"[WARN] Kartel Macro Bridge fallback aktif: {exc}")
        return fallback
