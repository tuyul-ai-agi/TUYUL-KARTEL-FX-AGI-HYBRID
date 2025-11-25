"""Hybrid fusion orchestrator coordinating full analysis cycles."""

from typing import Dict, Any

from .rlsi_module_v540 import (
    generate_rlsi_demo_frame,
    latest_rlsi_signal,
    tuyul_rlsi_pipeline,
)
from .tuyul_fusion_engine_v540 import run_fusion_layer12
from ..risk.adaptive_risk_calculator_v540 import calculate_risk
from ..reflective.meta_reflector_dispatch import run_meta_reflection


def run_full_fusion_cycle(pair: str, timeframe: str) -> Dict[str, Any]:
    """Run complete fusion cycle including risk and reflection analysis.
    
    Args:
        pair: Trading pair symbol.
        timeframe: Analysis timeframe.
        
    Returns:
        Dictionary with fusion metrics, risk calculations, and reflection data.
    """
    fusion_output = run_fusion_layer12(pair, timeframe)
    risk_output = calculate_risk(100000, 50)
    rlsi_frame = tuyul_rlsi_pipeline(generate_rlsi_demo_frame(pair, timeframe))
    rlsi_value, rlsi_interpretation, rlsi_status = latest_rlsi_signal(rlsi_frame)
    reflection = run_meta_reflection(fusion_output)
    return {
        "pair": pair,
        "conf12": fusion_output.conf12,
        "wlwci": fusion_output.wlwci,
        "rcadj": fusion_output.rcadj,
        "rlsi": {
            "latest": round(rlsi_value, 4),
            "interpretation": rlsi_interpretation,
            "status": rlsi_status,
        },
        "risk": risk_output,
        "reflection": reflection,
    }
