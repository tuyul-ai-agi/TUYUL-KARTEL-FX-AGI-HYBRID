"""Coherence monitor utility for Fusion Layer outputs."""

from __future__ import annotations

from typing import Dict


class CoherenceMonitor:
    """Evaluasi keselarasan antara skor Reflex, Fusion, dan WLWCI."""

    def evaluate(self, reflex_conf: float, fusion_conf: float, wlwci: float) -> Dict[str, float]:
        """Hitung indeks coherence sederhana.

        Args:
            reflex_conf: Nilai kepercayaan Reflex.
            fusion_conf: Nilai confidence Fusion.
            wlwci: Weighted layer-wise coherence index.

        Returns:
            Dictionary berisi coherence_index yang dibatasi antara 0 dan 1.
        """

        average_score = (reflex_conf + fusion_conf + wlwci) / 3
        coherence_index = max(0.0, min(1.0, round(average_score, 3)))
        return {"coherence_index": coherence_index}
