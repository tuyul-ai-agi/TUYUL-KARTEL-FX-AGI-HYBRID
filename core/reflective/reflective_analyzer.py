"""🧠 Reflective Analyzer – TUYUL FX AGI HYBRID."""

from datetime import UTC, datetime

from core.reflective.reflective_live_bridge import ReflectiveLiveBridge
from core.reflective.reflective_reasoner import ReflectiveReasoner
from core.reflective.reflective_status import ReflectiveStatus


def analyze_reflective_layers(pair: str, timeframe: str):
    """Snapshot analisa reflektif lintas layer."""

    print(f"🧩 Analisa reflektif real-time untuk {pair} [{timeframe}] ...")

    bridge_status = ReflectiveLiveBridge().ping_all()
    reasoning = ReflectiveReasoner().evaluate_cycle()
    status_snapshot = ReflectiveStatus().get_status()

    return {
        "pair": pair,
        "timeframe": timeframe,
        "bias": reasoning["bias"],
        "fusion_confidence": reasoning["fusion_confidence"],
        "wlwci": reasoning["wlwci"],
        "rcadj": reasoning["rcadj"],
        "integrity": bridge_status["integrity_index"],
        "coherence": bridge_status["coherence_score"],
        "latency_ms": bridge_status["latency_ms"],
        "regime_state": status_snapshot["regime_state"],
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }
