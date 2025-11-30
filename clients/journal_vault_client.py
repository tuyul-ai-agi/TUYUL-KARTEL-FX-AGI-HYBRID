"""
Journal Vault Client
--------------------
Client API untuk Journal Vault (meta-learning dan refleksi).
"""

from clients.vault_base_client import VaultBaseClient

class JournalVaultClient(VaultBaseClient):
    def __init__(self):
        super().__init__(base_url="https://api.journalvault.tuyulkartel.ai", api_key_env="JOURNAL_VAULT_KEY")

    def upload_reflection(self, reflection: dict):
        """Kirim hasil refleksi reasoning ke Journal Vault"""
        return self.post("reflection/upload", json=reflection)

    def get_recent_reflections(self, limit=5):
        """Ambil refleksi reasoning terakhir"""
        return self.get(f"reflection/recent?limit={limit}")

    def integrity_report(self):
        """Ambil laporan integritas reasoning terakhir"""
        return self.get("reflection/integrity")
