"""
Kartel Vault Client v6.0
-----------------------------------------
Stores bias matrices and reflective heuristics.
"""

from clients.vault_client_base import VaultClientBase

class KartelVaultClient(VaultClientBase):
    def __init__(self):
        super().__init__("reflective_repos/kartel_repo/vdd_regime_reflective.py", "kartel_vault")

    def get_bias_patterns(self):
        data = self.read()
        return [b for b in data if "bias" in b]
