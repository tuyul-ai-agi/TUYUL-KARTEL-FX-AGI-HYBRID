# ⚙️ FXVaultClientReflective — TUYUL FX AGI HYBRID v5.7.3r++
from .vault_client_base import VaultClientBase

class FXVaultClient(VaultClientBase):
    """Vault untuk data & strategi FX reflektif"""

    def __init__(self, endpoint, token=None):
        super().__init__("FXVault", endpoint, token)
        self.bias = None
        self.conf12 = 0.0

    async def update_bias(self, bias, conf):
        self.bias = bias
        self.conf12 = conf
        print(f"📊 [FXVault] Updated Bias: {bias}, CONF₁₂: {conf}")
        return await self.reflective_sync()

