from ..fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle
from ..adapters.vault_bridge_client import sync_vaults
from ..reflective.meta_reflector_dispatch import run_meta_reflection


class GPTBridgeHandler:
    def __init__(self):
        self.status = "Initialized"

    def run_analysis(self, pair: str, timeframe: str):
        """Terima perintah GPT (gas kan analisa) lalu jalankan reasoning lengkap."""
        fusion_output = run_full_fusion_cycle(pair, timeframe)
        sync_vaults()  # Sinkronkan hasil
        run_meta_reflection(fusion_output)
        return fusion_output

    def get_status(self):
        return {"bridge_status": self.status, "last_sync": "Vault updated"}
