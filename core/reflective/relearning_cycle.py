"""Relearning cycle for adaptive threshold adjustment."""

import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directory to path for standalone execution
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from core.adapters.vault_bridge_client import load_vault_feedback
else:
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


if __name__ == "__main__":
    """Run meta learning cycle when executed as a script."""
    print("🧠 Starting meta learning cycle...")
    try:
        result = relearn_from_vault()
        print(f"✅ Meta learning completed: {result['status']}")
        print(f"📊 Adjustments: {result['adjustments']}")
    except Exception as e:
        print(f"❌ Meta learning failed: {e}")
        exit(1)
