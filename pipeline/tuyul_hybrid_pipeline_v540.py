"""
🐺 TUYUL FX ULTRA WOLF — Hybrid AGI Pipeline v5.4.0
====================================================
Pipeline utama mengatur aliran analisis dari Reflex → Fusion → Risk → Reflective.
"""

from tuyul_fx_agi_hybrid.core.reflex.reflex_core_v540 import ReflexCoreV540
from tuyul_fx_agi_hybrid.modules.bridge_module_v540 import TuyulAgiBridgeV540
from tuyul_fx_agi_hybrid.core.reflective.reflective_cycle_core_v540 import ReflectiveCycleCoreV540
from tuyul_fx_agi_hybrid.core.bridge.vault_autosync_v541 import scan_and_sync

import asyncio

class TuyulHybridPipelineV540:
    def __init__(self):
        self.bridge = TuyulAgiBridgeV540()
        self.reflex = ReflexCoreV540()
        self.reflective = ReflectiveCycleCoreV540()

    async def run(self, pair="XAUUSD", timeframe="H4", balance=100000):
        print(f"\n🐺 Running TUYUL Hybrid Pipeline v5.4.0 — {pair} ({timeframe})")
        reflex_data = self.reflex.analyze(pair)
        fusion_output = await self.bridge.fusion_analyze(pair, timeframe)
        risk = await self.bridge.risk_calculate(balance, 120, pair)
        reflective = self.reflective.run_cycle(fusion_output.get("data", {}), reflex_data, risk.get("data", {}))
        scan_and_sync("/mnt/data")
        return {"fusion": fusion_output, "risk": risk, "reflective": reflective}

if __name__ == "__main__":
    asyncio.run(TuyulHybridPipelineV540().run())
