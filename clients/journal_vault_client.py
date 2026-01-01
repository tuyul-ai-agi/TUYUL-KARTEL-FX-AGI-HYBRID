"""
Journal Vault Client v6.0
-----------------------------------------
Handles reflective reasoning logs and coherence records.
"""

from clients.vault_client_base import VaultClientBase

class JournalVaultClient(VaultClientBase):
    def __init__(self):
        super().__init__("reflective_repos/journal_repo/quad_repo_sync.json", "journal_vault")

    def append_entry(self, entry):
        logs = self.read()
        logs.append(entry)
        self.write(logs)
