"""
Vault Diff Sync
---------------
Membandingkan dua vault dan menyinkronkan perubahan antar file JSON.
"""

import json
import os
from datetime import datetime
import shutil

class VaultDiffSync:
    def __init__(self, source_vault="vaults/fx_vault/", target_vault="vaults/journal_vault/"):
        self.source_vault = source_vault
        self.target_vault = target_vault

    def compare_and_sync(self):
        sync_log = []
        for file in os.listdir(self.source_vault):
            if not file.endswith(".json"):
                continue
            src_file = os.path.join(self.source_vault, file)
            tgt_file = os.path.join(self.target_vault, file)

            if not os.path.exists(tgt_file) or os.path.getmtime(src_file) > os.path.getmtime(tgt_file):
                shutil.copy2(src_file, tgt_file)
                sync_log.append({
                    "file": file,
                    "status": "updated",
                    "timestamp": datetime.utcnow().isoformat()
                })
        with open("logs/vault_diff_sync.log", "a") as log:
            for entry in sync_log:
                log.write(json.dumps(entry) + "\n")
        return sync_log
