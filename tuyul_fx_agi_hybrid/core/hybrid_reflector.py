"""Hybrid coordinator combining fusion and risk outputs."""

from .fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle
from .risk.volatility_regressor_v540 import detect_volatility_deviation


def run_hybrid_reflection(pair: str, timeframe: str):
    """Coordinate Reflex–Fusion–Risk reasoning into a final decision."""

    fusion_output = run_full_fusion_cycle(pair, timeframe)
    dvg = detect_volatility_deviation(fusion_output)
    status = "EXECUTE" if fusion_output["conf12"] >= 0.75 and dvg["DVG"] < 0.7 else "WAIT"
    return {
        "pair": pair,
        "conf12": fusion_output["conf12"],
        "wlwci": fusion_output["wlwci"],
        "rcadj": fusion_output["rcadj"],
        "dvg": dvg["DVG"],
        "status": status,
    }
