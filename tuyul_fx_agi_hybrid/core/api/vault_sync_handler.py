"""Vault synchronization API handler."""

from fastapi import APIRouter
from pydantic import BaseModel

from ...adapters.vault_bridge_client import sync_vaults

router = APIRouter()


class VaultSyncResponse(BaseModel):
    sync_status: str
    details: dict


@router.post("/sync", response_model=VaultSyncResponse)
def vault_sync() -> VaultSyncResponse:
    """Trigger vault synchronization across journal, knowledge, and hybrid stores."""

    result = sync_vaults()
    return VaultSyncResponse(sync_status="complete", details=result)
