"""Fusion Layer-12 API handler.

Exposes the Layer-12 fusion engine through FastAPI, returning confidence metrics
and reflex coherence adjustments for downstream consumers.
"""

from fastapi import APIRouter
from pydantic import BaseModel

from ...fusion.tuyul_fusion_engine_v540 import FusionResult, run_fusion_layer12

router = APIRouter()


class FusionRequest(BaseModel):
    pair: str
    timeframe: str


class FusionResponse(BaseModel):
    pair: str
    CONF12: float
    WLWCI: float
    RCAdj: float


@router.post("/run", response_model=FusionResponse)
def run_fusion(req: FusionRequest) -> FusionResponse:
    """Run the Fusion Layer-12 engine and return its metrics."""

    result: FusionResult = run_fusion_layer12(req.pair, req.timeframe)
    return FusionResponse(
        pair=req.pair,
        CONF12=result.conf12,
        WLWCI=result.wlwci,
        RCAdj=result.rcadj,
    )
