"""
🧾 Reflective Status – TUYUL FX AGI HYBRID
-----------------------------------------
Menyimpan hasil reflektif ke Journal Vault.
-----------------------------------------
"""

import json
import os
from datetime import datetime

LOG_PATH = "journal_repo/logs/reflective_status_log.json"

def update_status_log(result: dict):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    result["logged_at"] = datetime.utcnow().isoformat()
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write(",\n")
    print(f"🧾 Log reflektif tersimpan → {LOG_PATH}")

def get_reflective_status():
    if not os.path.exists(LOG_PATH):
        return {"status": "No log yet."}
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        logs = f.readlines()
    return {"status": "OK", "entries": len(logs)}
