"""
Fusion Confidence Core
----------------------
Hitung CONF₁₂ dan RCAdj berdasarkan korelasi antar layer reasoning.
"""

class FusionConfidenceCore:
    def __init__(self):
        pass

    def compute_confidence(self, reflex_score, fusion_score):
        conf12 = (reflex_score * 0.6 + fusion_score * 0.4)
        rcadj = (reflex_score + fusion_score) / 2
        return {
            "CONF12": round(conf12, 3),
            "RCAdj": round(rcadj, 3)
        }
