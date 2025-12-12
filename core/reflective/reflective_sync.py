"""
📦 Reflective Sync – TUYUL FX AGI HYBRID
-----------------------------------------
Sinkronisasi Quad Repo melalui API Vault.
-----------------------------------------
"""

import requests
from datetime import datetime

HYBRID_CORE_URL = "https://api.hybridcore.tuyulkartel.ai/v1"

def sync_quad_repo():
    url = f"{HYBRID_CORE_URL}/vault/sync"
    try:
        res = requests.get(url, timeout=20)
        data = res.json()
        print(f"🔗 Vault Sync → Integrity={data.get('integrity_index')}")
        return {
            "status": "Synced",
            "integrity_index": data.get("integrity_index"),
            "reflective_sync": data.get("reflective_sync"),
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        print("⚠️ Gagal sinkronisasi Vault:", e)
        return {"status": "Error", "integrity_index": 0.0, "reflective_sync": "failed"}
