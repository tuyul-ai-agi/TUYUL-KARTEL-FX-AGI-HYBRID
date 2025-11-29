"""
Reflective Cycle Core v5.4.0
----------------------------
Menjalankan siklus refleksi periodik untuk evaluasi hasil reasoning AGI.
"""

from __future__ import annotations

from typing import Any, Dict

from core.reflective.reflective_reasoner_v540 import ReflectiveReasoner
from core.reflective.relearning_cycle import RelearningCycle


class ReflectiveCycleCore:
    """Kelola siklus refleksi dan pemicuan relearning."""

    def __init__(self) -> None:
        self.reasoner = ReflectiveReasoner()
        self.relearn = RelearningCycle()

    def run_cycle(self, fusion_result: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluasi hasil fusion dan jalankan relearning jika perlu."""

        reflection = self.reasoner.evaluate(fusion_result)
        if reflection["Reflection"] == "Need Relearn":
            self.relearn.execute(reflection)
        return reflection


# Kompatibilitas nama kelas lama
ReflectiveCycleCoreV540 = ReflectiveCycleCore
