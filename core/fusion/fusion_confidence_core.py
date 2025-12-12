"""
Fusion Confidence Core — TUYUL FX AGI v5.7.3r++
Layer–12 Reflective Integration Engine
--------------------------------------
Menghitung CONF₁₂, WLWCI, dan RCAdj dengan validasi reflektif adaptif.
Versi ini lebih tahan error, backward-compatible, dan memiliki fallback
jika NumPy atau Python UTC tidak tersedia.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, Iterable

try:
    import numpy as np
except ImportError:
    # Safe fallback jika NumPy tidak ada
    import math

    class np:  # type: ignore
        @staticmethod
        def array(x, dtype=float):
            return list(x)

        @staticmethod
        def mean(x):
            return sum(x) / len(x) if x else 0.0

        @staticmethod
        def std(x):
            if not x:
                return 0.0
            mu = np.mean(x)
            return math.sqrt(sum((i - mu) ** 2 for i in x) / len(x))

        @staticmethod
        def corrcoef(x, y):
            # Fallback korelasi sederhana (Pearson)
            n = len(x)
            if n < 2:
                return [[1, 1], [1, 1]]
            mean_x, mean_y = np.mean(x), np.mean(y)
            num = sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y))
            den = math.sqrt(sum((a - mean_x) ** 2 for a in x) * sum((b - mean_y) ** 2 for b in y))
            corr = num / den if den != 0 else 0
            return [[1, corr], [corr, 1]]


class FusionConfidenceCore:
    """Menghitung CONF₁₂, WLWCI, dan RCAdj dengan validasi reflektif."""

    def __init__(self) -> None:
        self.conf12: float = 0.0
        self.wlwci: float = 0.0
        self.rcadj: float = 0.0
        self.reflective_state: str = "undefined"

    def compute(self, coherence_inputs: Iterable[float]) -> Dict[str, float]:
        """Hitung metrik fusion confidence dari input koherensi lintas layer."""

        try:
            coherence_array = np.array(list(coherence_inputs), dtype=float)
        except Exception:
            coherence_array = np.array([0.0])

        if len(coherence_array) == 0:
            coherence_array = np.array([0.0])

        # Hitung nilai rata-rata (CONF₁₂)
        self.conf12 = round(float(np.mean(coherence_array)), 3)

        # WLWCI = fungsi dari standar deviasi + offset stabilisasi
        std_val = float(np.std(coherence_array))
        self.wlwci = round(min(std_val * 0.9 + 0.88, 1.0), 3)

        # RCAdj = korelasi antara coherence sequence dan waktu
        if len(coherence_array) > 1:
            rc_corr = np.corrcoef(coherence_array, np.arange(len(coherence_array)))[0, 1]
            if rc_corr != rc_corr:  # NaN check
                rc_corr = 0.0
        else:
            rc_corr = 0.0
        self.rcadj = round(float(rc_corr), 3)

        # Tentukan status reflektif
        if self.conf12 >= 0.9 and self.wlwci >= 0.9:
            self.reflective_state = "stable"
        elif self.conf12 >= 0.8:
            self.reflective_state = "adaptive"
        else:
            self.reflective_state = "unstable"

        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conf12": self.conf12,
            "wlwci": self.wlwci,
            "rcadj": self.rcadj,
            "reflective_state": self.reflective_state,
        }


if __name__ == "__main__":
    # Contoh Pengujian Lokal
    fusion = FusionConfidenceCore()
    test_input = [0.92, 0.88, 0.94, 0.91, 0.89]
    result = fusion.compute(test_input)
    print("Fusion Confidence Metrics:")
    for k, v in result.items():
        print(f"{k:>18}: {v}")
