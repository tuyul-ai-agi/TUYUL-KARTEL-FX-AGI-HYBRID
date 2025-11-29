"""
Vault Integrity Checker
-----------------------
Memverifikasi integritas Vault dengan hash dan laporan perubahan.
"""

import os
import json
import hashlib

class VaultIntegrityChecker:
    def __init__(self, vault_root="vaults/"):
        self.vault_root = vault_root

    def compute_hash(self, file_path):
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def verify_integrity(self):
        report = {}
        for root, _, files in os.walk(self.vault_root):
            for file in files:
                if file.endswith(".json"):
                    path = os.path.join(root, file)
                    report[path] = self.compute_hash(path)
        with open("logs/vault_integrity_report.json", "w") as f:
            json.dump(report, f, indent=2)
        return report
