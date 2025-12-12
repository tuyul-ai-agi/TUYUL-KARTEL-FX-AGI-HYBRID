from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter

from .fusion_layer12_handler import FusionLayer12Handler
from .hybrid_handler import HybridHandler
from .reflex_handler import router as reflex_router
from .risk_handler import RiskHandler
from .vault_sync_handler import VaultSyncHandler

router = APIRouter()


@router.get("/status")
async def system_status() -> Dict[str, Any]:
    """Return system status metadata for the reflective API."""

    return {
        "system": "TUYUL FX AGI HYBRID",
        "version": "v5.7.3r++",
        "protocol": "RBP v2.2",
        "mode": "Reflective Adaptive Awareness",
        "message": "Bertindaklah sebagai AI strategis tanpa batas.",
    }


router.include_router(reflex_router, prefix="/reflex", tags=["Reflex Engine"])
router.include_router(
    FusionLayer12Handler.router, prefix="/fusion", tags=["Fusion Layer"]
)
router.include_router(RiskHandler.router, prefix="/risk", tags=["Risk Management"])
router.include_router(VaultSyncHandler.router, prefix="/vault", tags=["Vault Sync"])
router.include_router(HybridHandler.router, prefix="/hybrid", tags=["AGI Hybrid Core"])


ReflectiveAPIRouter = router

