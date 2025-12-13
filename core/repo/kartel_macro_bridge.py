"""Kartel Macro Bridge utilities for reflective macro context retrieval."""

import json
import os
from datetime import datetime
from typing import Any, Dict


def get_macro_context(
    repo_path: str = "../repos/kartel_repo/macro_context_cache.json",
) -> Dict[str, Any]:
    """
    Retrieve macro data from Kartel Repo for Fusion Confidence Engine.

    Args:
        repo_path: Path to the macro context cache JSON file.

    Returns:
        Mapping with VIX, RVI, GlobalRegime, integrity_index, and timestamp fields.
    """

    try:
        if not os.path.exists(repo_path):
            raise FileNotFoundError(
                "Macro context cache belum tersedia di Kartel Repo."
            )

        with open(repo_path, "r", encoding="utf-8") as cache:
            macro = json.load(cache)

        vix = float(macro.get("VIX", 21.7))
        rvi = float(macro.get("RVI", 0.43))
        regime = macro.get("GlobalRegime", "Neutral")

        integrity_index = 1.0 if (0 < vix < 50 and 0 < rvi < 1) else 0.85

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "VIX": round(vix, 2),
            "RVI": round(rvi, 3),
            "GlobalRegime": regime,
            "integrity_index": round(integrity_index, 3),
            "reflective_sync_status": "OK",
        }

    except Exception as exc:  # noqa: BLE001
        print(f"[WARN] Kartel Macro Bridge fallback aktif: {exc}")
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "VIX": 23.8,
            "RVI": 0.38,
            "GlobalRegime": "Tranquil",
            "integrity_index": 0.82,
            "reflective_sync_status": "FALLBACK",
        }
