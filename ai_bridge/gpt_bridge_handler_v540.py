"""
🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0
GPT Bridge Handler — Reflex–Cognition Integration Layer
"""

from datetime import datetime
from typing import Any, Dict

from adapters.vault_bridge_client import sync_vaults
from fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle
from reflective.meta_reflector_dispatch import run_meta_reflection


class GPTBridgeHandler:
    """Bridge handler for GPT commands to trigger full hybrid reasoning cycles."""

    def __init__(self) -> None:
        self.status = "Initialized"
        self.last_sync = None

    def run_analysis(self, pair: str, timeframe: str) -> Dict[str, Any]:
        """
        Execute complete reasoning analysis for a trading pair.
        Includes fusion cycle, vault sync, and meta reflection.
        """
        print(f"🐺 Running hybrid fusion analysis for {pair} [{timeframe}]...")
        fusion_output = run_full_fusion_cycle(pair, timeframe)

        sync_vaults()  # Synchronize results to vault
        run_meta_reflection(fusion_output)

        self.last_sync = datetime.utcnow().isoformat()
        self.status = "Completed"

        return {
            "pair": pair,
            "timeframe": timeframe,
            "fusion_output": fusion_output,
            "bridge_status": self.status,
            "last_sync": self.last_sync,
        }

    def get_status(self) -> Dict[str, str]:
        """Get current GPT bridge status."""
        return {
            "bridge_status": self.status,
            "last_sync": self.last_sync or "Not synced yet",
        }
