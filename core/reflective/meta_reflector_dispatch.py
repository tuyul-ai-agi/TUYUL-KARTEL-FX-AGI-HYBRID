"""Meta-reflective dispatch for automatic reasoning analysis."""

from __future__ import annotations

from typing import Any, Dict

from core.reflective.reflective_reasoner_v540 import ReflectiveReasoner


def run_meta_reflection(fusion_output: Any) -> Dict[str, Any]:
    """Execute automatic reflection on the latest reasoning output."""

    try:
        payload = getattr(fusion_output, "data", fusion_output)
        reasoner = ReflectiveReasoner()
        report = reasoner.evaluate(payload)
        return {"reflection_status": "ok", "report": report}
    except Exception as exc:  # pragma: no cover - defensive fallback
        return {"reflection_status": "error", "detail": str(exc)}
