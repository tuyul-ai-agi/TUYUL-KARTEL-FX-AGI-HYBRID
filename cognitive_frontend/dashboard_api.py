"""
Reflective Dashboard API v6.0
-----------------------------------------
Serves live reflective diagnostics and system coherence data
for visualization in the web UI.
"""

from fastapi import FastAPI

from clients.reflective_diagnostics import ReflectiveDiagnostics
from clients.hybrid_reflective_bridge_manager import HybridReflectiveBridgeManager

app = FastAPI(title="TUYUL-FX Reflective Dashboard API v6.0")

diag = ReflectiveDiagnostics()
bridge = HybridReflectiveBridgeManager()


@app.get("/status")
async def status():
    return {"status": "active", "version": "6.0.0", "bridge": "Reflective Hybrid Online"}


@app.get("/coherence")
async def coherence():
    return diag.check_coherence()


@app.get("/sync")
async def sync_all():
    result = bridge.sync_all()
    return {"sync_result": result}


@app.get("/logs")
async def logs():
    with open("logs/reflective_core_log.json") as f:
        return {"logs": f.read().splitlines()}
