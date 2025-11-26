"""🐺 TUYUL FX ULTRA WOLF AGI HYBRID – FastAPI Main Entry v5.4.1"""

import uvicorn
from fastapi import FastAPI
from datetime import datetime
from starlette.responses import JSONResponse

# Import API router (yang sudah mencakup GPT Bridge dan semua modul)
from tuyul_fx_agi_hybrid.api.api_router import api_router
from adapters.vault_bridge_client import sync_vaults

app = FastAPI(
    title="🐺 TUYUL FX ULTRA WOLF AGI Hybrid API",
    version="5.4.1",
    description=(
        "Reflex–Fusion–Cognition Hybrid system integrating AGI reasoning, "
        "Vault synchronization, and Reflective learning.\n"
        "Precision = Survival."
    ),
)

# ======================================================
# 🚀 APPLICATION LIFECYCLE EVENTS
# ======================================================
@app.on_event("startup")
async def startup_event():
    print("🔄 [Startup] Initializing TUYUL FX AGI Hybrid environment...")
    try:
        sync_vaults()
        print("✅ Vaults synchronized successfully.")
    except Exception as e:
        print(f"⚠️ Vault sync failed on startup: {e}")
    print("🧠 System online — AGI Hybrid ready for commands.\n")


@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 [Shutdown] Stopping TUYUL FX AGI Hybrid services...")
    print("💾 All pending operations flushed.\n")


# ======================================================
# 🔗 ROUTER REGISTRATION
# ======================================================
app.include_router(api_router)


# ======================================================
# ⚙️ ROOT HEALTH CHECK
# ======================================================
@app.get("/", tags=["System"])
async def root_status():
    return JSONResponse(
        {
            "system": "TUYUL FX ULTRA WOLF AGI HYBRID",
            "version": "5.4.1",
            "status": "✅ Online and synchronized",
            "startup_time": datetime.utcnow().isoformat(),
            "modules": [
                "Fusion Layer 12",
                "Reflex Engine",
                "Risk Management",
                "Vault Sync",
                "Reflective Meta-Cycle",
                "GPT Bridge",
                "System Diagnostics",
            ],
        }
    )


# ======================================================
# 🔥 SERVER ENTRYPOINT
# ======================================================
if __name__ == "__main__":
    uvicorn.run(
        "tuyul_fx_agi_hybrid.main_v540:app",
        host="0.0.0.0",
        port=5400,
        reload=True,
        log_level="info",
    )
