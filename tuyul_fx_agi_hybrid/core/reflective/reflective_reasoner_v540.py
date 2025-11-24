"""Reflective reasoning and bias analysis module."""

from typing import Any, Dict

from ..vaults.reflection_output import save_reflection_report


def analyze_reflection(last_conf12: float, current_conf12: float) -> Dict[str, Any]:
    """Analyze confidence delta and determine bias direction.
    
    Args:
        last_conf12: Previous CONF12 value.
        current_conf12: Current CONF12 value.
        
    Returns:
        Dictionary containing delta and bias direction.
    """
    delta = round(current_conf12 - last_conf12, 3)
    bias = "positive" if delta > 0 else "negative"
    report = {"delta_conf12": delta, "bias": bias}
    save_reflection_report(report)
    return report
