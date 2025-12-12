"""
Fusion Confidence Core (Extended) — TUYUL FX AGI v5.7.3r++
----------------------------------------------------------
Layer–12 Reflective Fusion Engine with Journal Vault Logging.
Menghitung CONF₁₂, WLWCI, RCAdj, dan integrasi langsung ke Journal Vault JSON.

Refleksi ini memungkinkan sistem:
- Melacak stabilitas lintas-layer
- Menilai bias regime (Bullish / Bearish / Neutral)
- Menyimpan catatan reflektif tiap siklus
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable

try:
    import numpy as np
except ImportError:
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
            n = len(x)
            if n < 2:
                return [[1, 1], [1, 1]]
            mean_x, mean_y = np.mean(x), np.mean(y)
            num = sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y))
            den = math.sqrt(sum((a - mean_x) ** 2 for a in x) * sum((b - mean_y) ** 2 for b in y))
            corr = num / den if den != 0 else 0
            return [[1, corr], [corr, 1]]


class FusionConfidenceCore:
    """Core reflektif untuk menghitung dan merekam metrik CONF₁₂, WLWCI, RCAdj."""

    def __init__(self, vault_path: str = "journal/fusion_confidence_record_v573r++.json") -> None:
        self.vault_path = Path(vault_path)
        self.vault_path.parent.mkdir(parents=True, exist_ok=True)

        self.conf12 = 0.0
        self.wlwci = 0.0
        self.rcadj = 0.0
        self.integrity_index = 0.0
        self.reflective_state = "undefined"
        self.regime_bias = "neutral"

    def compute(self, coherence_inputs: Iterable[float], regime_hint: str = "neutral") -> Dict[str, float]:
        """Hitung metrik reflektif lintas layer."""

        coherence_array = np.array(list(coherence_inputs), dtype=float)
        if len(coherence_array) == 0:
            coherence_array = np.array([0.0])

        # Layer–12 metrics
        self.conf12 = round(float(np.mean(coherence_array)), 3)
        self.wlwci = round(min(float(np.std(coherence_array) * 0.9 + 0.88), 1.0), 3)

        # Correlation Adjusted Coherence (RCAdj)
        if len(coherence_array) > 1:
            rc_corr = np.corrcoef(coherence_array, np.arange(len(coherence_array)))[0, 1]
            if rc_corr != rc_corr:  # NaN guard
                rc_corr = 0.0
        else:
            rc_corr = 0.0
        self.rcadj = round(float(rc_corr), 3)

        # Reflective state logic
        if self.conf12 >= 0.9 and self.wlwci >= 0.9:
            self.reflective_state = "stable"
        elif self.conf12 >= 0.8:
            self.reflective_state = "adaptive"
        else:
            self.reflective_state = "unstable"

        # Regime awareness
        self.regime_bias = regime_hint.lower()
        if self.regime_bias not in ["bullish", "bearish", "neutral"]:
            self.regime_bias = "neutral"

        # Integrity index (composite stability factor)
        self.integrity_index = round((self.conf12 + self.wlwci + abs(self.rcadj)) / 3, 3)

        # Compose record
        record: Dict[str, float | str] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conf12": self.conf12,
            "wlwci": self.wlwci,
            "rcadj": self.rcadj,
            "integrity_index": self.integrity_index,
            "reflective_state": self.reflective_state,
            "regime_bias": self.regime_bias,
            "system_version": "v5.7.3r++",
        }

        # Save reflective record
        self._save_to_vault(record)

        return record

    def _save_to_vault(self, record: Dict[str, float | str]) -> None:
        """Simpan hasil reflektif ke Journal Vault JSON."""

        try:
            if self.vault_path.exists():
                with open(self.vault_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
                    if not isinstance(existing, list):
                        existing = [existing]
            else:
                existing = []

            existing.append(record)
            with open(self.vault_path, "w", encoding="utf-8") as f:
                json.dump(existing[-200:], f, indent=2)
        except Exception as exc:  # pragma: no cover - I/O safeguard
            print(f"⚠️ [Reflective Vault Write Error]: {exc}")


if __name__ == "__main__":
    fusion = FusionConfidenceCore()
    sample_data = [0.91, 0.89, 0.94, 0.88, 0.92]
    result = fusion.compute(sample_data, regime_hint="bullish")

    print("🧠 TUYUL FX Fusion Reflective Output v5.7.3r++")
    for k, v in result.items():
        print(f"{k:>18}: {v}")
