"""
Fusion Layer-12 Handler
-----------------------
Endpoint API untuk hasil reasoning Layer 12 AGI Fusion.
"""

from fastapi import APIRouter
from core.analytics.coherence_monitor import CoherenceMonitor

router = APIRouter()
monitor = CoherenceMonitor()


@router.get("/fusion")
def get_fusion_status(reflex_conf: float = 0.9, fusion_conf: float = 0.88, wlwci: float = 0.95):
    result = monitor.evaluate(reflex_conf, fusion_conf, wlwci)
    return {
        "layer": "Fusion Layer-12",
        "fusion_confidence": result["coherence_index"],
        "state": result["state"]
    }
