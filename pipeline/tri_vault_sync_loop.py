"""
Tri Vault Sync Loop
-------------------
Sinkronisasi otomatis antara FX, Kartel, dan Journal Vaults.
"""

from core.vaults.vault_diff_sync import VaultDiffSync

class TriVaultSyncLoop:
    def __init__(self):
        self.sync_fx_journal = VaultDiffSync("vaults/fx_vault/", "vaults/journal_vault/")
        self.sync_kartel_journal = VaultDiffSync("vaults/kartel_vault/", "vaults/journal_vault/")

    def run(self):
        fx_result = self.sync_fx_journal.compare_and_sync()
        kartel_result = self.sync_kartel_journal.compare_and_sync()
        return {
            "fx_to_journal": fx_result,
            "kartel_to_journal": kartel_result
        }
