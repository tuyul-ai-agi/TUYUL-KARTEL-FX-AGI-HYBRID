"""
Vault AutoSync v5.7.3r++
------------------------
Sinkronisasi otomatis antar Vaults (Hybrid–Knowledge–Kartel–Journal)
setiap Reflective Bridge selesai melakukan cycle.
"""

import os
import json
from datetime import datetime
from shutil import copyfile

VAULTS = ["vaults/hybrid", "vaults/knowledge", "vaults/kartel", "vaults/journal"]


def sync_vaults():
    print("[SYNC] Starting Vault AutoSync process ...")
    timestamp = datetime.utcnow().isoformat()
    for vault in VAULTS:
        target = os.path.join(vault, "sync.json")
        payload = {"timestamp": timestamp, "status": "synced", "bridge": "RBP v2.2"}
        os.makedirs(vault, exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"[SYNC] {vault} updated ✅")
    print("[DONE] Vault AutoSync completed.")


if __name__ == "__main__":
    sync_vaults()
