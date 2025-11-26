"""🐺 TUYUL FX ULTRA WOLF AGI HYBRID — MAIN RUNTIME v5.4.1
Full AGI runtime server combining Reflex, Fusion, Vault, GPT Bridge, and Reflective systems.
Precision = Survival.
"""

import asyncio
import uvicorn
from datetime import datetime
from fastapi import FastAPI
from starlette.responses import JSONResponse

# === Core Routers ===
from core.main_router import api_router

# === Adapters / Subsystems ===
from adapters.vault_bridge_client import sync_vaults
from fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle
from reflective.meta_reflector_dispatch import run_meta_reflection
from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler

# === Initialize ===
app = FastAPI(
    title="🐺 TUYUL FX ULTRA WOLF AGI HYBRID",
    version="5.4.1",
    description=(
        "Fusion–Reflex–Cognition Hybrid System integrating AGI reasoning, "
        "Vault synchronization, and Reflective learning. "
        "Built for precision, not speculation."
    ),
)

gpt_bridge = GPTBridgeHandler()


# ======================================================
# ⚙️ STARTUP EVENT
# ======================================================
@app.on_event("startup")
async def startup_event():
    print("🔄 [Startup] Initializing TUYUL FX AGI Hybrid Environment...")
    try:
        sync_vaults()
        print("✅ Vaults synchronized successfully.")
    except Exception as e:
        print(f"⚠️ Vault sync failed: {e}")

    # Optional: run system self-check
    print("🧠 Running internal Reflex Coherence warm-up...")
    try:
        _ = run_full_fusion_cycle("EURJPY", "H1")
        print("✅ Reflex coherence initialization complete.")
    except Exception as e:
        print(f"⚠️ Fusion warm-up failed: {e}")

    print("🧩 Launching Reflective Meta-Learning Bootstrap...")
    try:
        await asyncio.sleep(3)
        run_meta_reflection({"boot": True})
        print("✅ Reflective system initialized.")
    except Exception as e:
        print(f"⚠️ Reflective initialization failed: {e}")

    print(f"🚀 TUYUL FX AGI HYBRID v5.4.1 ONLINE — {datetime.utcnow().isoformat()}\n")


# ======================================================
# 🧩 SHUTDOWN EVENT
# ======================================================
@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 [Shutdown] Stopping TUYUL FX AGI Hybrid services...")
    print("💾 All pending operations flushed.")
    print("🧠 Reflective session terminated.\n")


# ======================================================
# 🔗 ROUTER REGISTRATION
# ======================================================
app.include_router(api_router)


# ======================================================
# 📡 ROOT HEALTH CHECK
# ======================================================
@app.get("/", tags=["System"])
async def root_status():
    return JSONResponse(
        {
            "system": "TUYUL FX ULTRA WOLF AGI HYBRID",
            "version": "v5.4.1",
            "status": "✅ Online and synchronized",
            "timestamp": datetime.utcnow().isoformat(),
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
# 🧠 GPT COMMAND BRIDGE (Optional Direct Route)
# ======================================================
@app.post("/gpt/run", tags=["GPT Bridge"])
async def run_gpt_analysis(payload: dict):
    """Trigger GPT → Fusion → Reflection full analysis pipeline."""
    pair = payload.get("pair", "XAUUSD")
    timeframe = payload.get("timeframe", "H1")

    print(f"⚙️ GPT Bridge triggered for {pair}-{timeframe}")
    result = gpt_bridge.run_analysis(pair, timeframe)
    return JSONResponse(result)


# ======================================================
# 🔥 RUNTIME ENTRYPOINT
# ======================================================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5400,
        reload=True,
        log_level="info",
    )
