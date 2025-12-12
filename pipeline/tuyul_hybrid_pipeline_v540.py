"""
Tuyul Hybrid Pipeline v5.7.3r++
------------------------------
Pipeline Reflex → Fusion → Reflective dengan integrasi WLWCI & Quantum.
"""

from __future__ import annotations

import pandas as pd

from clients import FXVaultClient, JournalVaultClient
from core.fusion import (
    FinalOutputReflectiveEngine,
    QuantumFusionAdapter,
    ReflectiveFusionOrchestrator,
)
from core.reflex.reflex_core_v540 import ReflexCore
from core.fushion.tuyul_fusion_engine_v540 import TuyulFusionEngine
from core.reflective.reflective_cycle_core import ReflectiveCycleCore
from core.reflective.reflective_cycle_core_v540 import ReflectiveCycleCore
from core.vdd.vddhybrid_module_v540 import VDDHybridModule


class TuyulHybridPipeline:
    def __init__(self):
        self.reflex = ReflexCore()
        self.orchestrator = ReflectiveFusionOrchestrator()
        self.reflective = ReflectiveCycleCore()
        self.vdd = VDDHybridModule()
        self.final_output = FinalOutputReflectiveEngine()
        self.quantum_adapter = QuantumFusionAdapter()
        self.fx = FXVaultClient()
        self.journal = JournalVaultClient()

    @staticmethod
    def _macro_signature(df: pd.DataFrame) -> dict:
        returns = df.get("close", pd.Series(dtype=float)).pct_change().dropna()
        volatility = returns.std() if not returns.empty else 0.0
        mean_move = returns.mean() if not returns.empty else 0.0
        conf_macro = max(0.6, min(0.99, 0.95 - volatility))
        rcadj = round(mean_move * 10, 3)
        return {"conf_macro": round(conf_macro, 3), "rcadj": rcadj}

    def run(self, pair: str = "XAUUSD"):
        feed = self.fx.get_latest_feed(pair)
        df = pd.DataFrame(feed["data"])

        reflex_out = self.reflex.analyze(df)
        fusion_out = self.fusion.run(reflex_out["RLSI"] / 100, 0.9, df)
        reflective_out = self.reflective.execute()
        vdd_out = self.vdd.detect_regime(df, reflex_out["RLSI"], fusion_out["FusionConfidence"], 0.9)
        macro_data = self._macro_signature(df)
        fusion_state = self.orchestrator.run_fusion_cycle(reflex_out, macro_data)
        quantum_snapshot = self.quantum_adapter.analyze_coherence(
            [reflex_out.get("conf_reflex", 0.9), macro_data["conf_macro"], fusion_state["rcadj"]]
        )
        reflective_out = self.reflective.run_cycle(fusion_state)
        vdd_out = self.vdd.detect_regime(
            df, reflex_out["RLSI"], fusion_state["fusion_confidence"], macro_data["conf_macro"]
        )

        fused_payload = {
            "pair": pair,
            "reflex": reflex_out,
            "fusion": fusion_state,
            "quantum": quantum_snapshot,
            "reflective": reflective_out,
            "vdd": vdd_out,
        }

        self.journal.upload_reflection(fused_payload)
        self.final_output.generate(fusion_state, bias=reflective_out.get("bias", "Bullish continuation"))

        return {"pair": pair, "fusion_confidence": fusion_state["fusion_confidence"], "vdd": vdd_out}
