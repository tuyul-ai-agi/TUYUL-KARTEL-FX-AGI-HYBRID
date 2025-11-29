"""
FX Vault Client
---------------
Client API untuk membaca dan menulis data ke FX Vault.
"""

from clients.vault_base_client import VaultBaseClient

class FXVaultClient(VaultBaseClient):
    def __init__(self):
        super().__init__(base_url="https://api.fxvault.tuyulkartel.ai", api_key_env="FX_VAULT_KEY")

    def get_latest_feed(self, pair="XAUUSD"):
        """Ambil feed terbaru dari FX Vault"""
        return self.get(f"feed/latest?pair={pair}")

    def push_fusion_result(self, fusion_data: dict):
        """Kirim hasil fusion AGI ke FX Vault"""
        return self.post("fusion/upload", json=fusion_data)

    def sync(self):
        """Sinkronisasi FX Vault"""
        return self.get("sync")
