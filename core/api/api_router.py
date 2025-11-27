"""
🐺 TUYUL FX AGI HYBRID – Central API Router v5.4.1-H (Production-Ready)
Menyatukan modul Fusion, Reflex, Risk, Vault, Reflective, GPT, dan System
ke dalam satu FastAPI router terintegrasi untuk orkestra AGI TUYUL HYBRID.
"""

import asyncio
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse
from datetime import datetime
from collections import deque

# Import modular routers
from .fusion_layer12_handler import router as fusion_router
from .hybrid_handler import router as hybrid_router
from .reflex_handler import router as reflex_router
from .risk_handler import router as risk_router
from .vault_sync_handler import router as vault_router
from .reflective_handler import router as reflective_router
from .system_handler import router as system_router
from .gpt_bridge_handler_v540 import GPTBridgeHandler

# ==========================
# ⚙️ Metadata & Diagnostics
# ==========================
__version__ = "5.4.1-H"
__build__ = datetime.utcnow().strftime("%Y%m%d%H%M")
__author__ = "TUYUL LAB 🧠⚡"

latencies = deque(maxlen=100)  # store recent latency stats
gpt_bridge = GPTBridgeHandler()  # init GPT bridge
api_router = APIRouter()  # main router instance

# ==========================
# 🔀 Include Modular Routers
# ==========================
api_router.include_router(fusion_router, prefix="/fusion", tags=["Fusion"])
api_router.include_router(hybrid_router, prefix="/hybrid", tags=["Hybrid"])
api_router.include_router(reflex_router, prefix="/reflex", tags=["Reflex"])
api_router.include_router(risk_router, prefix="/risk", tags=["Risk"])
api_router.include_router(vault_router, prefix="/vault", tags=["Vault"])
api_router.include_router(reflective_router, prefix="/reflective", tags=["Reflective"])
api_router.include_router(system_router, prefix="/system", tags=["System"])

# ==========================
# 🧠 GPT Bridge Endpoints
# ==========================
@api_router.post("/gpt/bridge", tags=["GPT Bridge"])
async def gpt_bridge_entry(payload: dict):
    """Trigger full reasoning cycle via GPT bridge."""
    pair = payload.get("pair")
    timeframe = payload.get("timeframe")
    result = await asyncio.to_thread(gpt_bridge.run_analysis, pair, timeframe)
    return JSONResponse(result)

@api_router.get("/gpt/status", tags=["GPT Bridge"])
async def gpt_bridge_status():
    """Get GPT bridge current status."""
    return JSONResponse(gpt_bridge.get_status())

# ==========================
# ⚙️ Middleware & Logging
# ==========================
@api_router.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.utcnow()
    try:
        response = await call_next(request)
    except Exception as exc:
        print(f"❌ Exception in {request.url.path}: {exc}")
        return JSONResponse(
            {"error": str(exc), "path": request.url.path, "timestamp": start_time.isoformat()},
            status_code=500,
        )
    process_time = (datetime.utcnow() - start_time).total_seconds() * 1000
    latencies.append(process_time)
    print(
        f"[{start_time.isoformat()}] {request.method} {request.url.path} "
        f"→ {response.status_code} ({process_time:.2f}ms)"
    )
    response.headers["X-Process-Time-ms"] = str(round(process_time, 2))
    return response

# ==========================
# 🧩 Performance Diagnostics
# ==========================
@api_router.get("/system/perf", tags=["System"])
async def get_perf_stats():
    """Get performance metrics (avg latency)."""
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0
    return {
        "avg_latency_ms": round(avg_latency, 2),
        "samples": len(latencies),
        "version": __version__,
        "build": __build__,
        "timestamp": datetime.utcnow().isoformat(),
    }

# ==========================
# 📘 OpenAPI Spec Exposer
# ==========================
@api_router.get("/openapi.yaml", tags=["System"], include_in_schema=False)
async def get_openapi_spec():
    """Expose AGI Hybrid OpenAPI Spec."""
    return FileResponse("docs/openapi_tuyul_agi_hybrid.yml", media_type="application/yaml")

# ==========================
# ✅ Root Diagnostic Route
# ==========================
@api_router.get("/", tags=["System"])
async def root_status():
    """Root diagnostic route for TUYUL FX AGI Hybrid."""
    return JSONResponse(
        {
            "system": "TUYUL FX ULTRA WOLF AGI HYBRID",
            "version": __version__,
            "build": __build__,
            "author": __author__,
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
            "avg_latency_ms": round(sum(latencies) / len(latencies), 2) if latencies else 0.0,
            "timestamp": datetime.utcnow().isoformat(),
        }
    )
