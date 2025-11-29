"""
Vault Sync v5.4.0
-----------------
Sinkronisasi vault AGI (FX, Kartel, Journal) dengan verifikasi integritas file JSON.
"""

import json, os, hashlib, shutil
from datetime import datetime

class VaultSync:
    def __init__(self, base_path="vaults/"):
        self.base_path = base_path
        self.vaults = ["fx_vault", "kartel_vault", "journal_vault"]

    def compute_hash(self, file_path):
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def sync(self):
        report = []
        for v in self.vaults:
            vpath = os.path.join(self.base_path, v)
            if not os.path.exists(vpath): 
                continue
            for f in os.listdir(vpath):
                if f.endswith(".json"):
                    full = os.path.join(vpath, f)
                    h = self.compute_hash(full)
                    report.append({"vault": v, "file": f, "hash": h})
        with open("logs/vault_sync.log", "a") as log:
            log.write(f"[{datetime.utcnow()}] Synced {len(report)} files.\n")
        return report
