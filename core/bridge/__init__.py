# TUYUL FX AGI HYBRID v5.7.3r++
# Reflective Bridge Loader — RBP v2.2
from .api_bridge_core import ApiBridgeCore
from .reflex_fusion_bridge_connector import ReflexFusionBridgeConnector
from .tuyul_fx_vault_bridge_v573r import ReflectiveVaultBridge

__version__ = "v5.7.3r++"
__protocol__ = "RBP v2.2"
__all__ = ["ApiBridgeCore", "ReflexFusionBridgeConnector", "ReflectiveVaultBridge"]

print("🔗 Reflective Bridge Layer Initialized — TUYUL FX v5.7.3r++")
