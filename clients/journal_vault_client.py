# 🧾 JournalVaultClientReflective — TUYUL FX AGI HYBRID v5.7.3r++
from .vault_client_base import VaultClientBase
import json, datetime, os

class JournalVaultClient(VaultClientBase):
    """Vault reflektif untuk penyimpanan hasil meta-learning & integrity logs"""

    def __init__(self, endpoint, token=None):
        super().__init__("JournalVault", endpoint, token)
        os.makedirs("journal", exist_ok=True)

    async def write_reflective_log(self, data):
        ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        path = f"journal/reflective_log_{ts}.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"🧠 [JournalVault] Log saved → {path}")
        return await self.reflective_sync()
