"""
Final Output Layer-12 Engine v5.4.1
-----------------------------------
Menghasilkan output final dari Fusion Layer (CONF₁₂, RCAdj, WLWCI, Integrity Index).
"""

from core.analytics.coherence_reflective_monitor import ReflectiveCoherenceMonitor

class FinalOutput12Engine:
    def __init__(self):
        self.monitor = ReflectiveCoherenceMonitor()

    def generate_output(self, reflex_conf, fusion_conf, wlwci):
        coherence = self.monitor.evaluate(fusion_conf, wlwci, reflex_conf)
        integrity_index = round((reflex_conf + fusion_conf + wlwci) / 3, 3)
        fusion_confidence = round(coherence["avg_coherence"], 3)
        return {
            "CONF12": fusion_confidence,
            "RCAdj": reflex_conf,
            "WLWCI": wlwci,
            "IntegrityIndex": integrity_index,
            "RegimeState": 0 if integrity_index > 0.85 else 1
        }
