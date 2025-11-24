"""Central API router for TUYUL FX AGI Hybrid.

Combines Fusion, Reflex, Risk, and Vault endpoints into a single FastAPI router
that can be included in the main application.
"""

from fastapi import APIRouter

from .fusion_layer12_handler import router as fusion_router
from .hybrid_handler import router as hybrid_router
from .reflex_handler import router as reflex_router
from .risk_handler import router as risk_router
from .vault_sync_handler import router as vault_router

api_router = APIRouter()
api_router.include_router(fusion_router, prefix="/fusion", tags=["Fusion"])
api_router.include_router(hybrid_router, prefix="/hybrid", tags=["Hybrid"])
api_router.include_router(reflex_router, prefix="/reflex", tags=["Reflex"])
api_router.include_router(risk_router, prefix="/risk", tags=["Risk"])
api_router.include_router(vault_router, prefix="/vault", tags=["Vault"])
