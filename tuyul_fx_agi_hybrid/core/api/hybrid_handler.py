"""Hybrid Fusion API handler for full AGI analysis cycles."""

from datetime import datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

from ..fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle

router = APIRouter()


class FullFusionRequest(BaseModel):
    pair: str
    timeframe: str


class FullFusionResponse(BaseModel):
    pair: str
    conf12: float
    wlwci: float
    rcadj: float
    rc_value: float
    bias_delta: float
    timestamp: str


def _build_response(payload: dict) -> FullFusionResponse:
    reflection = payload.get("reflection", {})
    report = reflection.get("report", {}) if isinstance(reflection, dict) else {}
    bias_delta = float(report.get("delta_conf12", 0.0)) if isinstance(report, dict) else 0.0
    return FullFusionResponse(
        pair=str(payload.get("pair", "")),
        conf12=float(payload.get("conf12", 0.0)),
        wlwci=float(payload.get("wlwci", 0.0)),
        rcadj=float(payload.get("rcadj", 0.0)),
        rc_value=float(payload.get("rcadj", 0.0)),
        bias_delta=bias_delta,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@router.post("/runFullFusion", response_model=FullFusionResponse)
def run_full_fusion(req: FullFusionRequest) -> FullFusionResponse:
    """Run the full fusion-reflex cycle and return fusion metrics."""

    output = run_full_fusion_cycle(req.pair, req.timeframe)
    return _build_response(output)


@router.get("/getFusionLayer12", response_model=FullFusionResponse)
def get_fusion_layer12(pair: str = "XAUUSD", timeframe: str = "H1") -> FullFusionResponse:
    """Fetch Layer-12 fusion metrics for the given pair and timeframe."""

    output = run_full_fusion_cycle(pair, timeframe)
    return _build_response(output)
