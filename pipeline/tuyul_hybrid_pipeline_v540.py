"""
Tuyul Hybrid Pipeline v5.4.0
----------------------------
Pipeline utama untuk reasoning Reflex → Fusion → Reflective dan sinkronisasi Vault.
"""

from core.reflex.reflex_core_v540 import ReflexCore
from core.fushion.tuyul_fusion_engine_v540 import TuyulFusionEngine
from core.reflective.reflective_cycle_core_v540 import ReflectiveCycleCore
from core.vdd.vddhybrid_module_v540 import VDDHybridModule
from clients import FXVaultClient, JournalVaultClient
import pandas as pd

class TuyulHybridPipeline:
    def __init__(self):
        self.reflex = ReflexCore()
        self.fusion = TuyulFusionEngine()
        self.reflective = ReflectiveCycleCore()
        self.vdd = VDDHybridModule()
        self.fx = FXVaultClient()
        self.journal = JournalVaultClient()

    def run(self, pair="XAUUSD"):
        feed = self.fx.get_latest_feed(pair)
        df = pd.DataFrame(feed["data"])

        reflex_out = self.reflex.analyze(df)
        fusion_out = self.fusion.run(reflex_out["RLSI"] / 100, 0.9, df)
        reflective_out = self.reflective.run_cycle(fusion_out)
        vdd_out = self.vdd.detect_regime(df, reflex_out["RLSI"], fusion_out["FusionConfidence"], 0.9)

        self.journal.upload_reflection({
            "pair": pair,
            "reflex": reflex_out,
            "fusion": fusion_out,
            "reflective": reflective_out,
            "vdd": vdd_out
        })

        return {"pair": pair, "fusion_confidence": fusion_out["FusionConfidence"], "vdd": vdd_out}
