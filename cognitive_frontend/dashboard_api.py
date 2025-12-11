# ⚡ Dashboard API Layer — TUYUL FX AGI HYBRID v5.7.3r++
# Endpoint JSON untuk akses dashboard reflektif via RBP v2.2
from fastapi import FastAPI
import json, os

api = FastAPI(title="TUYUL Reflective API v5.7.3r++")

@api.get("/metrics")
def get_metrics():
    path = "logs/reflective_diagnostics.json"
    if not os.path.exists(path):
        return {"error": "No data"}
    with open(path, "r") as f:
        logs = json.load(f)[-10:]
    return {"count": len(logs), "last_reflection_score": logs[-1]["reflection_score"], "logs": logs}
