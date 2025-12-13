# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Reflective Layer Strength Index (RLSI)
# ------------------------------------------------------------
# Mengukur kekuatan reflektif lintas time-frame.
# ============================================================

from statistics import mean
from datetime import datetime
import json
import os


def compute_rlsi(price_data):
    """Menghitung Reflective Layer Strength Index."""
    if len(price_data) < 5:
        raise ValueError("Data tidak cukup untuk menghitung RLSI.")
    rlsi = (mean(price_data[-5:]) / max(price_data)) * 100
    result = {
        "rlsi_value": round(rlsi, 2),
        "reflective_mode": "HYBRID_BALANCE",
        "integrity": 0.91,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    os.makedirs("journal_repo", exist_ok=True)
    with open("journal_repo/rlsi_reflective.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"🧮 [RLSI] Value={result['rlsi_value']} | Integrity={result['integrity']}")
    return result
