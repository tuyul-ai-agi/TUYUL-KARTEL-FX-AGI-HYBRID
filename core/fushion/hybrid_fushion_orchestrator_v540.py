"""
🐺 TUYUL FX ULTRA WOLF v5.4.1 — Hybrid Fusion Orchestrator
Integrates RLSI, VDDHybrid, Reflex, and Risk Engine in unified Fusion pipeline.
"""

import asyncio
import json
import datetime
import redis

from modules.vddhybrid_module_v540 import VDDHybridModule
from modules.rlsi_module_v540 import ReflexLiquidityShiftIndex
from modules.bridge_module_v540 import TuyulAgiBridgeV540
from modules.vault_autosync_v541 import VaultAutoSync


class HybridFusionOrchestrator:
    def __init__(self):
        self.redis_client = redis.Redis(host="localhost", port=6379, db=0)
        self.vdd = VDDHybridModule()
        self.rlsi = ReflexLiquidityShiftIndex()
        self.bridge = TuyulAgiBridgeV540()
        self.vault = VaultAutoSync()
        self.last_output = None

    async def fuse(self, market_data: dict):
        """Main Fusion logic combining VDDHybrid, RLSI, and Reflex data."""
        # 1️⃣ Regime Detection (Macro)
        vdd_signal = await self.vdd.detect_regime()

        # 2️⃣ RLSI Calculation (Micro)
        rlsi_value = await self.rlsi.calculate(market_data)

        # 3️⃣ Adaptive Fusion Weighting
        weights = {0: (0.8, 0.2), 1: (0.4, 0.6), 2: (0.1, 0.9)}
        w_micro, w_macro = weights[vdd_signal["RegimeState"]]
        conf12 = round(
            w_micro * rlsi_value + w_macro * vdd_signal["Probabilities"].get(vdd_signal["RegimeState"], 0.5),
            3,
        )

        # 4️⃣ Create Fusion Output
        timestamp = datetime.datetime.utcnow().isoformat()
        fusion_output = {
            "FusionConfidence": conf12,
            "RLSI": rlsi_value,
            "RegimeState": vdd_signal["RegimeState"],
            "RegimeName": vdd_signal["RegimeName"],
            "VIX_DXY_Prob": vdd_signal["Probabilities"],
            "Timestamp": timestamp,
        }

        # 5️⃣ Save to Redis + Journal + Vault
        self.last_output = fusion_output
        self.redis_client.publish("fusion_output", json.dumps(fusion_output))
        await self.bridge.fusion_save_journal(fusion_output)
        self.vault.save(fusion_output)

        return fusion_output


# ===============================================================
# 🔬 TEST MODE
# ===============================================================
async def run_fusion_cycle(market_data):
    orchestrator = HybridFusionOrchestrator()
    result = await orchestrator.fuse(market_data)
    print("Fusion Output:", json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    sample_data = {"VIX": [16.5, 18.2, 21.0], "DXY": [103.2, 104.1, 104.8]}
    asyncio.run(run_fusion_cycle(sample_data))
