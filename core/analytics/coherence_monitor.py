"""
Coherence Monitor
-----------------
Mengukur keselarasan antara Reflex dan Fusion Layer berdasarkan nilai CONF₁₂ & WLWCI.
"""


class CoherenceMonitor:
    def evaluate(self, reflex_conf: float, fusion_conf: float, wlwci: float):
        coherence_index = (reflex_conf * 0.4 + fusion_conf * 0.4 + wlwci * 0.2)
        state = "Stable" if coherence_index > 0.85 else "Volatile"
        return {
            "coherence_index": round(coherence_index, 3),
            "state": state
        }
