"""🐺 Hybrid Fusion API Handler for TUYUL FX AGI v5.4.1-HYBRID."""

from datetime import datetime, timezone
from fastapi import APIRouter
from pydantic import BaseModel

from ..fushion.hybrid_fushion_orchestrator_v540 import run_full_fusion_cycle
from ..adapters.vault_bridge_client import sync_vaults
from ..journal.journal_bridge import log_event

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
    reflection_gain: float
    timestamp: str


def _build_response(payload: dict) -> FullFusionResponse:
    reflection = payload.get("reflection", {})
    report = reflection.get("report", {}) if isinstance(reflection, dict) else {}

    bias_delta = float(report.get("delta_conf12", 0.0))
    reflection_gain = float(report.get("gain", 0.0))

    return FullFusionResponse(
        pair=str(payload.get("pair", "")),
        conf12=float(payload.get("conf12", 0.0)),
        wlwci=float(payload.get("wlwci", 0.0)),
        rcadj=float(payload.get("rcadj", 0.0)),
        rc_value=float(payload.get("rc", payload.get("rcadj", 0.0))),
        bias_delta=bias_delta,
        reflection_gain=reflection_gain,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@router.post(
    "/runFullFusion",
    response_model=FullFusionResponse,
    operation_id="runFullFusion",
    summary="Run full AGI Fusion-Reflex analysis cycle",
)
def run_full_fusion(req: FullFusionRequest) -> FullFusionResponse:
    """Execute the complete AGI Fusion reasoning cycle and sync results."""
    log_event(f"[Fusion Layer] Starting full fusion cycle for {req.pair}-{req.timeframe}")
    output = run_full_fusion_cycle(req.pair, req.timeframe)

    # Sync vaults automatically after successful reasoning
    try:
        sync_vaults()
        log_event(f"[Vault Sync] ✅ Fusion results synced for {req.pair}-{req.timeframe}")
    except Exception as e:
        log_event(f"[Vault Sync] ⚠️ Failed to sync after fusion: {e}")

    return _build_response(output)


@router.get(
    "/getFusionLayer12",
    response_model=FullFusionResponse,
    operation_id="getFusionLayer12",
    summary="Fetch Layer-12 Fusion metrics (CONF₁₂, WLWCI, RCAdj)",
)
def get_fusion_layer12(pair: str = "XAUUSD", timeframe: str = "H1") -> FullFusionResponse:
    """Fetch Layer-12 fusion metrics for the given pair and timeframe."""
    output = run_full_fusion_cycle(pair, timeframe)
    return _build_response(output)
