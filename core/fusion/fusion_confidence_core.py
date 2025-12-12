# Fusion Confidence Core — TUYUL FX v5.7.3r++
from datetime import UTC, datetime
from typing import Iterable

import numpy as np


class FusionConfidenceCore:
    """Menghitung CONF₁₂, WLWCI, dan RCAdj dengan validasi reflektif."""

    def __init__(self) -> None:
        self.conf12 = 0.0
        self.wlwci = 0.0
        self.rcadj = 0.0

    def compute(self, coherence_inputs: Iterable[float]):
        """Hitung metrik fusion confidence berbasis daftar coherence input."""

        coherence_array = np.array(list(coherence_inputs), dtype=float)
        if coherence_array.size == 0:
            coherence_array = np.array([0.0])

        self.conf12 = round(float(np.mean(coherence_array)), 3)
        self.wlwci = round(float(np.std(coherence_array) * 0.9 + 0.88), 3)
        self.rcadj = round(
            float(np.corrcoef(coherence_array, np.arange(coherence_array.size))[0, 1]), 3
        )

        reflective_state = "stable" if self.conf12 >= 0.9 else "adaptive"

        return {
            "timestamp": datetime.now(UTC).isoformat(),
            "conf12": self.conf12,
            "wlwci": self.wlwci,
            "rcadj": self.rcadj,
            "reflective_state": reflective_state,
        }
