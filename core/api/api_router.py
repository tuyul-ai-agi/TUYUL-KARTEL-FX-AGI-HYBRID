"""
API Router
----------
Mengatur routing endpoint FastAPI untuk AGI Hybrid.
"""

from fastapi import APIRouter

from .reflex_handler import router as reflex_router
from .fusion_layer12_handler import router as fusion_router
from .risk_handler import router as risk_router
from .vault_sync_handler import router as vault_router

router = APIRouter()
router.include_router(reflex_router, prefix="/reflex", tags=["Reflex"])
router.include_router(fusion_router, prefix="/fusion", tags=["Fusion"])
router.include_router(risk_router, prefix="/risk", tags=["Risk"])
router.include_router(vault_router, prefix="/vault", tags=["Vault"])
