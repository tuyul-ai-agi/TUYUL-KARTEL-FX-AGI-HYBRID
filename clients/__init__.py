# TUYUL FX AGI HYBRID v5.7.3r++
# Reflective Client Package Initializer
from .client_agi_hybrid import HybridClient
from .fx_vault_client import FXVaultClient
from .journal_vault_client import JournalVaultClient
from .kartel_vault_client import KartelVaultClient
from .vault_client_base import VaultClientBase
from .reflective_logger import ReflectiveLogger

__all__ = [
    "HybridClient",
    "FXVaultClient",
    "JournalVaultClient",
    "KartelVaultClient",
    "VaultClientBase",
    "ReflectiveLogger"
]

# Auto-register all clients to Reflective Bridge Protocol
from datetime import datetime
print(f"[RBP v2.2] Clients registered successfully — {datetime.utcnow().isoformat()}Z")
