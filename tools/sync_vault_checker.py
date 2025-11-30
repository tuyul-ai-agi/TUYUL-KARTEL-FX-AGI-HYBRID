"""
Sync Vault Checker
------------------
Mengecek status sinkronisasi antara FX, Kartel, dan Journal Vaults.
"""

import os
import json
from datetime import datetime

class SyncVaultChecker:
    def __init__(self, fx_vault="vaults/fx_vault/", kartel_vault="vaults/kartel_vault/", journal_vault="vaults/journal_vault/"):
        self.fx = fx_vault
        self.kartel = kartel_vault
        self.journal = journal_vault

    def _compare(self, dir1, dir2):
        diff = []
        for f in os.listdir(dir1):
            path1 = os.path.join(dir1, f)
            path2 = os.path.join(dir2, f)
            if not os.path.exists(path2) or os.path.getmtime(path1) > os.path.getmtime(path2):
                diff.append(f)
        return diff

    def run_check(self):
        fx_journal_diff = self._compare(self.fx, self.journal)
        kartel_journal_diff = self._compare(self.kartel, self.journal)
        report = {
            "fx_to_journal_unsynced": fx_journal_diff,
            "kartel_to_journal_unsynced": kartel_journal_diff,
            "timestamp": datetime.utcnow().isoformat()
        }
        with open("logs/vault_sync.log", "a") as f:
            f.write(json.dumps(report) + "\n")
        return report


if __name__ == "__main__":
    checker = SyncVaultChecker()
    print(checker.run_check())
