"""
Tuyul Fusion Engine v5.4.0
--------------------------
Engine utama untuk reasoning fusion AGI Hybrid.
"""

import json
from datetime import datetime
from core.fushion.hybrid_fusion_orchestrator_v540 import HybridFusionOrchestrator

class TuyulFusionEngine:
    def __init__(self):
        self.orchestrator = HybridFusionOrchestrator()

    def run(self, reflex_conf, wl_wci, df):
        result = self.orchestrator.orchestrate(reflex_conf, wl_wci, df)
        result["timestamp"] = datetime.utcnow().isoformat()

        with open("vaults/fx_vault/fusion_journal.json", "w") as f:
            json.dump(result, f, indent=2)

        return result
