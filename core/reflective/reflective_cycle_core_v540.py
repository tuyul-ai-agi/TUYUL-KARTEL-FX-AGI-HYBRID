"""
Reflective Cycle Core v5.4.0
----------------------------
Menjalankan siklus refleksi periodik untuk evaluasi hasil reasoning AGI.
"""

from core.reflective.reflective_reasoner_v540 import ReflectiveReasoner
from core.reflective.relearning_cycle import RelearningCycle

class ReflectiveCycleCore:
    def __init__(self):
        self.reasoner = ReflectiveReasoner()
        self.relearn = RelearningCycle()

    def run_cycle(self, fusion_result):
        reflection = self.reasoner.evaluate(fusion_result)
        if reflection["Reflection"] == "Need Relearn":
            self.relearn.execute(reflection)
        return reflection
