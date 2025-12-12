"""
Bridge Module v5.7.3r++
----------------------
Menjembatani data antar layer Reflex–Fusion–Reflective.
"""

from core.reflex.reflex_core_v540 import ReflexCore
from core.fushion.tuyul_fusion_engine_v540 import TuyulFusionEngine
from core.reflective.reflective_cycle_core import ReflectiveCycleCore
from core.fusion import ReflectiveFusionOrchestrator
from core.reflective.reflective_cycle_core_v540 import ReflectiveCycleCore


class BridgeModule:
    def __init__(self):
        self.reflex = ReflexCore()
        self.fusion = ReflectiveFusionOrchestrator()
        self.reflective = ReflectiveCycleCore()

    def execute(self, df):
        reflex_result = self.reflex.analyze(df)
        fusion_result = self.fusion.run(reflex_result["RLSI"] / 100, 0.92, df)
        reflection = self.reflective.execute()
        macro_data = {
            "conf_macro": reflex_result.get("conf_reflex", 0.9),
            "rcadj": reflex_result.get("rcadj", 0.0),
        }
        fusion_result = self.fusion.run_fusion_cycle(reflex_result, macro_data)
        reflection = self.reflective.run_cycle(fusion_result)
        return {
            "reflex": reflex_result,
            "fusion": fusion_result,
            "reflective": reflection,
        }
