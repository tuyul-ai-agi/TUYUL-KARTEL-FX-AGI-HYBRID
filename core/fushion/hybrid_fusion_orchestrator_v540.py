"""
Hybrid Fusion Orchestrator v5.4.0
---------------------------------
Orkestrasi reasoning antara Reflex, Smart Money, dan WLWCI → Final Fusion.
"""

from core.fushion.fusion_confidence_core import FusionConfidenceCore
from core.analytics.smart_money_detector import SmartMoneyDetector

class HybridFusionOrchestrator:
    def __init__(self):
        self.conf_core = FusionConfidenceCore()
        self.smart_detector = SmartMoneyDetector()

    def orchestrate(self, reflex_conf, wl_wci, df):
        smart = self.smart_detector.summarize_bias(df)
        fusion_score = 0.8 if smart["bias"] == "BUY" else 0.7
        result = self.conf_core.compute_confidence(reflex_conf, fusion_score)
        result["SmartMoney"] = smart
        result["WLWCI"] = wl_wci
        return result
