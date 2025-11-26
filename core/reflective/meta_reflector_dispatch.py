"""Meta-reflective dispatch for automatic reasoning analysis."""

from typing import Dict, Any

from .reflective_reasoner_v540 import analyze_reflection


def run_meta_reflection(fusion_output: Any) -> Dict[str, Any]:
    """Execute automatic reflection on the latest reasoning output.
    
    Args:
        fusion_output: Output from fusion engine with conf12 attribute.
        
    Returns:
        Dictionary with reflection status and report.
    """
    try:
        last_conf12 = 0.75
        report = analyze_reflection(last_conf12, fusion_output.conf12)
        return {"reflection_status": "ok", "report": report}
    except Exception as e:
        return {"reflection_status": "error", "detail": str(e)}
