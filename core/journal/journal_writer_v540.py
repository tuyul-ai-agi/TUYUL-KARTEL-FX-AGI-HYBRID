"""
Journal Writer v5.4.0
---------------------
Menulis hasil reasoning AGI ke Journal Vault.
"""

import json
from datetime import datetime
import os


class JournalWriter:
    def __init__(self, vault_path="vaults/journal_vault/"):
        self.vault_path = vault_path
        os.makedirs(vault_path, exist_ok=True)


class JournalWriter:
    def __init__(self, vault_path="vaults/journal_vault/"):
        self.vault_path = vault_path
        os.makedirs(vault_path, exist_ok=True)

    def write_entry(self, data: dict):
        data["timestamp"] = datetime.utcnow().isoformat()
        file_path = os.path.join(self.vault_path, "fusion_journal.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        return {"status": "written", "path": file_path}
