"""
Fusion Confidence Core
----------------------
Hitung CONF₁₂ dan RCAdj berdasarkan korelasi antar layer reasoning.
"""

from __future__ import annotations

from typing import Dict


class FusionConfidenceCore:
    """Kalkulator sederhana untuk CONF12 dan RCAdj."""

    def compute_confidence(self, reflex_score: float, fusion_score: float) -> Dict[str, float]:
        """Hitung confidence fusion dan penyesuaian refleks.

        Args:
            reflex_score: Skor kepercayaan dari Reflex Layer.
            fusion_score: Skor hasil gabungan signal lainnya.

        Returns:
            Dictionary dengan nilai CONF12 dan RCAdj yang telah dibulatkan.
        """

        conf12 = (reflex_score * 0.6) + (fusion_score * 0.4)
        rcadj = (reflex_score + fusion_score) / 2
        return {"CONF12": round(conf12, 3), "RCAdj": round(rcadj, 3)}
