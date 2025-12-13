"""
Reflective Data Bridge for VDD (v5.7.8)
Fetches VIX and related macro signals through the JIT plugin layer and
provides normalized snapshots to VDD feature/regime modules.
"""

from datetime import datetime
from typing import Dict, Optional


def _ts() -> str:
    return datetime.utcnow().isoformat() + "Z"


def fetch_vix_snapshot(source: Optional[str] = None) -> Dict[str, float]:
    """
    Placeholder for JIT plugin call (api_twelvedata_com__jit_plugin).
    Returns a normalized snapshot for VDD processing.
    """
    # TODO: wire to actual plugin/bridge once available.
    return {
        "vix": 19.5,
        "rvi": 0.41,
        "term_structure": "Contango",
        "timestamp": _ts(),
        "source": source or "api_twelvedata_com__jit_plugin",
    }


def normalize_snapshot(snapshot: Dict[str, float]) -> Dict[str, float]:
    """Ensure required keys exist and types are numeric where needed."""
    return {
        "vix": float(snapshot.get("vix", 0.0)),
        "rvi": float(snapshot.get("rvi", 0.0)),
        "term_structure": snapshot.get("term_structure", "Unknown"),
        "timestamp": snapshot.get("timestamp", _ts()),
        "source": snapshot.get("source", "api_twelvedata_com__jit_plugin"),
    }
