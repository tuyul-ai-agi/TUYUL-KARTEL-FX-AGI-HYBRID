"""
TwelveData Feed Sync v6.0
-----------------------------------------
Fetches live market data and syncs it into fx_vault.
"""

from clients.fx_vault_client import FXVaultClient
from clients.tuyul_data_bridge import TuyulDataBridge

def sync():
    fx = FXVaultClient()
    bridge = TuyulDataBridge()
    data = bridge.fetch("GBP/USD", "1h")
    fx.write(data.get("values", []))
    return {"status": "synced", "records": len(data.get("values", []))}
