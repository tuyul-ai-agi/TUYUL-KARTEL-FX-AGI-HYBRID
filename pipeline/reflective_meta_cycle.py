"""
Reflective Meta Cycle
---------------------
Siklus meta-learning yang memperbarui model GPT dan parameter VDD berdasarkan hasil refleksi terbaru.
"""

from clients import JournalVaultClient
from core.vdd.vdd_conf_model_v543 import VDDConfModel

class ReflectiveMetaCycle:
    def __init__(self):
        self.journal = JournalVaultClient()
        self.vdd_conf = VDDConfModel()

    def execute(self):
        reflections = self.journal.get_recent_reflections(limit=5)
        latest_reflection = reflections[0] if reflections else {}
        new_state = latest_reflection.get("vdd", {}).get("RegimeState", "Tranquil")
        new_conf = self.vdd_conf.adjust_params(new_state)
        return {"updated_config": new_conf, "based_on": new_state}
