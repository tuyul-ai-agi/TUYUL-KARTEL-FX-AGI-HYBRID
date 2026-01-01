"""
Reflective Diagnostics v6.0
-----------------------------------------
Analyzes system coherence, bias health, and memory loop states.
"""

from clients.journal_vault_client import JournalVaultClient
from clients.reflective_logger import ReflectiveLogger
from statistics import mean

class ReflectiveDiagnostics:
    def __init__(self):
        self.journal = JournalVaultClient()
        self.logger = ReflectiveLogger()

    def check_coherence(self):
        entries = self.journal.read()
        coherence_values = [e.get("coherence", 0.9) for e in entries]
        avg_coh = round(mean(coherence_values), 3)
        self.logger.log(f"Coherence Average: {avg_coh}")
        return {"avg_coherence": avg_coh, "state": "stable" if avg_coh >= 0.92 else "unstable"}
