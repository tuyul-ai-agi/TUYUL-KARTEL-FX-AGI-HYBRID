"""
FX Vault Client v6.0
-----------------------------------------
Manages reflective market data and trading blueprints.
"""

from clients.vault_client_base import VaultClientBase

class FXVaultClient(VaultClientBase):
    def __init__(self):
        super().__init__("reflective_repos/fx_repo/fusion_journal.json", "fx_vault")

    def get_blueprints(self):
        data = self.read()
        return [entry for entry in data if "blueprint" in entry]

