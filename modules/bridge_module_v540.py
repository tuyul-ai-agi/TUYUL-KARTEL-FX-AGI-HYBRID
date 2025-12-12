"""
Bridge Module v5.4.0
--------------------
Menjembatani data antar layer Reflex–Fusion–Reflective.
"""

from core.reflex.reflex_core_v540 import ReflexCore
from core.fushion.tuyul_fusion_engine_v540 import TuyulFusionEngine
from core.reflective.reflective_cycle_core import ReflectiveCycleCore

class BridgeModule:
    def __init__(self):
        self.reflex = ReflexCore()
        self.fusion = TuyulFusionEngine()
        self.reflective = ReflectiveCycleCore()

    def execute(self, df):
        reflex_result = self.reflex.analyze(df)
        fusion_result = self.fusion.run(reflex_result["RLSI"] / 100, 0.92, df)
        reflection = self.reflective.execute()
        return {
            "reflex": reflex_result,
            "fusion": fusion_result,
            "reflective": reflection
        }

