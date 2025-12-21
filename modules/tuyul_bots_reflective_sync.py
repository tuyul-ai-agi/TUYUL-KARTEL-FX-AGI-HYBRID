"""Internal TUYUL Bots reflective bridge adaptor.

This module replaces external JIT plugin calls for Quad Repo sync with a
local bridge that leans on the reflective sync primitives in the codebase.
It keeps network access optional so automated tests do not require Redis
or remote services.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional

from core.reflective.reflective_sync import ReflectiveSync

try:  # Redis bridge is optional for tests
    from bots import tuyulbot_bridge_client as bridge_client
except Exception:  # pragma: no cover - fallback when Redis is unavailable
    bridge_client = None


@dataclass
class BridgeSnapshot:
    hybrid_to_vault: str = "synced"
    vault_to_kartel: str = "synced"
    kartel_to_journal: str = "synced"
    integrity_index: float = 0.95
    coherence_drift: str = "Stable"
    reflection_score: float = 0.95
    regime_adaptation: str = "Normal"
    latency_ms: int = 0
    reflective_state: str = "stable"
    reflective_sync: str = "OK"

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ReflectiveBridgeSync:
    """Run Quad Repo sync through the TUYUL Bots reflective bridge."""

    def __init__(self, reflective_sync: Optional[ReflectiveSync] = None):
        self.reflective_sync = reflective_sync or ReflectiveSync()

    def run_full_sync(self, meta_state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        meta_state = meta_state or {"bias_drift": 0.02, "reflective_state": "stable"}
        sync_payload = self.reflective_sync.run_sync(meta_state)

        snapshot = BridgeSnapshot(
            integrity_index=self._read_integrity_index(),
            coherence_drift=self._coherence_drift(meta_state),
            reflection_score=self._reflection_score(meta_state),
            latency_ms=sync_payload["latency_ms"],
            reflective_state=sync_payload["reflective_state"],
        )

        self._broadcast(sync_payload, snapshot)
        return snapshot.as_dict()

    @staticmethod
    def _coherence_drift(meta_state: Dict[str, Any]) -> str:
        drift = abs(float(meta_state.get("bias_drift", 0)))
        return "Stable" if drift < 0.08 else "Shifted"

    @staticmethod
    def _reflection_score(meta_state: Dict[str, Any]) -> float:
        drift = abs(float(meta_state.get("bias_drift", 0)))
        base_score = 0.96
        penalty = min(drift * 0.5, 0.05)
        return round(max(0.9, base_score - penalty), 3)

    @staticmethod
    def _read_integrity_index() -> float:
        if bridge_client is None:
            return 0.95

        try:
            integrity = bridge_client.read_vault_integrity()
            if integrity:
                return float(integrity)
        except Exception:
            return 0.95

        return 0.95

    @staticmethod
    def _broadcast(sync_payload: Dict[str, Any], snapshot: BridgeSnapshot) -> None:
        if bridge_client is None:
            return

        packet = {
            "timestamp": sync_payload["timestamp"],
            "reflective_state": sync_payload["reflective_state"],
            "latency_ms": sync_payload["latency_ms"],
            "integrity_index": snapshot.integrity_index,
            "coherence_drift": snapshot.coherence_drift,
        }

        for channel in ("hybrid_sync", "vault_sync", "kartel_sync", "journal_sync"):
            try:
                bridge_client.publish_event(channel, packet)
            except Exception:
                continue
