"""🐺 TUYUL FX AGI Hybrid – Central API Router v5.4.1

Combines Fusion, Reflex, Risk, Vault, Reflective, GPT, and System endpoints
into a unified FastAPI router for AGI orchestration.
"""

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from datetime import datetime

# Import modular routers
from .fusion_layer12_handler import router as fusion_router
from .hybrid_handler import router as hybrid_router
from .reflex_handler import router as reflex_router
from .risk_handler import router as risk_router
from .vault_sync_handler import router as vault_router
from .reflective_handler import router as reflective_router
from .system_handler import router as system_router
from .gpt_bridge_handler_v540 import GPTBridgeHandler

# Initialize GPT Bridge
gpt_bridge = GPTBridgeHandler()

# Initialize main router
api_router = APIRouter()

# Include sub-routers
api_router.include_router(fusion_router, prefix="/fusion", tags=["Fusion"])
api_router.include_router(hybrid_router, prefix="/hybrid", tags=["Hybrid"])
api_router.include_router(reflex_router, prefix="/reflex", tags=["Reflex"])
api_router.include_router(risk_router, prefix="/risk", tags=["Risk"])
api_router.include_router(vault_router, prefix="/vault", tags=["Vault"])
api_router.include_router(reflective_router, prefix="/reflective", tags=["Reflective"])
api_router.include_router(system_router, prefix="/system", tags=["System"])

# ========================
# 🧠 GPT Bridge Endpoints
# ========================
@api_router.post("/gpt/bridge", tags=["GPT Bridge"])
async def gpt_bridge_entry(payload: dict):
    """Trigger full reasoning cycle via GPT bridge."""
    pair = payload.get("pair")
    timeframe = payload.get("timeframe")
    result = gpt_bridge.run_analysis(pair, timeframe)
    return JSONResponse(result)


@api_router.get("/gpt/status", tags=["GPT Bridge"])
async def gpt_bridge_status():
    """Get GPT bridge current status."""
    return JSONResponse(gpt_bridge.get_status())


# ========================
# ⚙️ Middleware Diagnostics
# ========================
@api_router.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).total_seconds() * 1000
    print(
        f"[{start_time.isoformat()}] {request.method} {request.url.path} "
        f"→ {response.status_code} ({process_time:.2f}ms)"
    )
    response.headers["X-Process-Time-ms"] = str(round(process_time, 2))
    return response


# ========================
# ✅ Root Diagnostic Route
# ========================
@api_router.get("/", tags=["System"])
async def root_status():
    """Root diagnostic route for TUYUL FX AGI Hybrid."""
    return JSONResponse(
        {
            "system": "TUYUL FX ULTRA WOLF AGI HYBRID",
            "version": "v5.4.1",
            "modules": [
                "Fusion",
                "Reflex",
                "Risk",
                "Vault",
                "Reflective",
                "GPT Bridge",
                "System",
            ],
            "status": "🧠 Online and synchronized",
            "timestamp": datetime.utcnow().isoformat(),
        }
    )
