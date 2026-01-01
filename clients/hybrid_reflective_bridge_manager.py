"""
Hybrid Reflective Bridge Manager v6.0
-----------------------------------------
Core orchestrator linking all reflective clients.
"""

from clients.fx_vault_client import FXVaultClient
from clients.kartel_vault_client import KartelVaultClient
from clients.journal_vault_client import JournalVaultClient
from clients.reflective_diagnostics import ReflectiveDiagnostics
from clients.reflective_logger import ReflectiveLogger

class HybridReflectiveBridgeManager:
    def __init__(self):
        self.fx = FXVaultClient()
        self.kartel = KartelVaultClient()
        self.journal = JournalVaultClient()
        self.logger = ReflectiveLogger()
        self.diag = ReflectiveDiagnostics()

    def sync_all(self):
        self.logger.log("Starting Reflective Bridge Sync...")
        fx_data = self.fx.get_blueprints()
        kartel_bias = self.kartel.get_bias_patterns()
        coherence = self.diag.check_coherence()

        result = {
            "fx_entries": len(fx_data),
            "kartel_bias": len(kartel_bias),
            "coherence_state": coherence
        }
        self.logger.log(f"Bridge Sync Complete: {result}")
        return result
