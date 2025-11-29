"""
Hybrid Fusion Orchestrator v5.4.0
---------------------------------
Orkestrasi reasoning antara Reflex, Smart Money, dan WLWCI → Final Fusion.
"""

from __future__ import annotations

from typing import Any, Dict

from core.fushion.fusion_confidence_core import FusionConfidenceCore
from core.analytics.smart_money_detector import SmartMoneyDetector


class HybridFusionOrchestrator:
    """Kombinasikan input Reflex, Smart Money, dan WLWCI menjadi metrik fusion."""

    def __init__(self) -> None:
        self.conf_core = FusionConfidenceCore()
        self.smart_detector = SmartMoneyDetector()

    def orchestrate(self, reflex_conf: float, wl_wci: float, df) -> Dict[str, Any]:
        """Jalankan orkestrasi fusion sederhana.

        Args:
            reflex_conf: Confidence dari Reflex layer.
            wl_wci: Weighted layer-wise coherence index.
            df: DataFrame atau objek data yang dapat dianalisis Smart Money.

        Returns:
            Dictionary dengan CONF12, RCAdj, detail Smart Money, dan WLWCI.
        """

        smart = self.smart_detector.summarize_bias(df)
        fusion_score = 0.8 if smart.get("bias") == "BUY" else 0.7
        result = self.conf_core.compute_confidence(reflex_conf, fusion_score)
        result["SmartMoney"] = smart
        result["WLWCI"] = wl_wci
        return result
