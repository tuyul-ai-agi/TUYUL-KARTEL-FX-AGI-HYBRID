"""
Vault Sync Handler
------------------
Sinkronisasi antar vault (FX ↔ Kartel ↔ Journal).
"""

from fastapi import APIRouter
from ai_bridge.vault_autosync_v541 import VaultAutoSync

router = APIRouter()
sync = VaultAutoSync()


@router.get("/sync")
def sync_vaults():
    result = sync.sync_all()
    return {"status": "Vaults synchronized", "result": result}
