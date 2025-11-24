"""Relearning cycle for adaptive threshold adjustment."""

from typing import Dict, Any

from ..adapters.vault_bridge_client import load_vault_feedback


def relearn_from_vault() -> Dict[str, Any]:
    """Retrieve reasoning feedback and adjust adaptive thresholds.
    
    Returns:
        Dictionary with status and adjusted threshold values.
    """
    feedback = load_vault_feedback()
    adjustments = {
        "ema_weight": round(0.9 + feedback.get("ema_bias", 0) * 0.05, 3),
        "rc_threshold": round(0.75 + feedback.get("rc_delta", 0) * 0.05, 3),
    }
    return {"status": "updated", "adjustments": adjustments}
