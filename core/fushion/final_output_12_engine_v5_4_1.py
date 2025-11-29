"""
Final Output Layer-12 Engine v5.4.1
-----------------------------------
Menghasilkan output final dari Fusion Layer (CONF₁₂, RCAdj, WLWCI, Integrity Index).
"""

from __future__ import annotations

from typing import Any, Dict

from core.analytics.coherence_monitor import CoherenceMonitor


class FinalOutput12Engine:
    """Generator output akhir untuk Layer-12."""

    def __init__(self) -> None:
        self.monitor = CoherenceMonitor()

    def generate_output(self, reflex_conf: float, fusion_conf: float, wlwci: float) -> Dict[str, Any]:
        """Kalkulasi indeks integritas dan coherence final.

        Args:
            reflex_conf: Skor kepercayaan Reflex.
            fusion_conf: Skor Fusion.
            wlwci: Weighted layer-wise coherence index.

        Returns:
            Struktur dictionary dengan CONF12, RCAdj, WLWCI, IntegrityIndex, dan RegimeState.
        """

        coherence = self.monitor.evaluate(reflex_conf, fusion_conf, wlwci)
        integrity_index = round((reflex_conf + fusion_conf + wlwci) / 3, 3)
        fusion_confidence = round(coherence["coherence_index"], 3)
        return {
            "CONF12": fusion_confidence,
            "RCAdj": reflex_conf,
            "WLWCI": wlwci,
            "IntegrityIndex": integrity_index,
            "RegimeState": 0 if integrity_index > 0.85 else 1,
        }
