"""
TUYUL-FX Quantum Hybrid Reflective Client Package
Version: v6.0.0
-------------------------------------------------
Unified interface for all reflective bridge clients.
Performs initialization, integrity checks, and runtime registration.
"""

from datetime import datetime
from clients.client_agi_hybrid import AGIHybridClient
from clients.fx_vault_client import FXVaultClient
from clients.journal_vault_client import JournalVaultClient
from clients.kartel_vault_client import KartelVaultClient
from clients.vault_client_base import VaultClientBase
from clients.reflective_logger import ReflectiveLogger
from clients.reflective_diagnostics import ReflectiveDiagnostics

__version__ = "6.0.0"
__bridge_protocol__ = "RCP6"
__author__ = "TUYUL Reflective Systems Division"
__runtime_init__ = datetime.utcnow().isoformat()

__all__ = [
    "AGIHybridClient",
    "FXVaultClient",
    "JournalVaultClient",
    "KartelVaultClient",
    "VaultClientBase",
    "ReflectiveLogger",
    "ReflectiveDiagnostics",
]

# ----------------------------------------------------------------------
# 🧠 Reflective Bridge Initialization
# ----------------------------------------------------------------------

logger = ReflectiveLogger()
diag = ReflectiveDiagnostics()

try:
    fx = FXVaultClient()
    journal = JournalVaultClient()
    kartel = KartelVaultClient()
    agi = AGIHybridClient()

    # Reflective handshake
    logger.log(f"Reflective clients registered successfully — {datetime.utcnow().isoformat()}Z")
    coh_state = diag.check_coherence()

    print(f"[RCP6] ✅ TUYUL-FX Reflective Client Suite initialized (v6.0.0)")
    print(f"       Bridge coherence status: {coh_state['state']} ({coh_state['avg_coherence']})")
except Exception as e:
    logger.log(f"❌ Reflective initialization failed: {e}", level="ERROR")
    print(f"[RCP6 ERROR] Initialization failed: {e}")
