"""GPT bridge handler for executing complete analysis cycles."""

from typing import Any, Dict

from fusion.hybrid_fusion_orchestrator_v540 import run_full_fusion_cycle
from adapters.vault_bridge_client import sync_vaults
from reflective.meta_reflector_dispatch import run_meta_reflection


class GPTBridgeHandler:
    """Bridge handler for GPT commands to trigger full reasoning cycles."""

    def __init__(self) -> None:
        self.status = "Initialized"

    def run_analysis(self, pair: str, timeframe: str) -> Dict[str, Any]:
        """Execute complete reasoning analysis for a trading pair.

        Args:
            pair: Trading pair symbol.
            timeframe: Analysis timeframe.

        Returns:
            Complete fusion output with analysis results.
        """
        fusion_output = run_full_fusion_cycle(pair, timeframe)
        sync_vaults()  # Synchronize results to vault
        run_meta_reflection(fusion_output)
        return fusion_output

    def get_status(self) -> Dict[str, str]:
        """Get current bridge status.

        Returns:
            Dictionary with bridge status information.
        """
        return {"bridge_status": self.status, "last_sync": "Vault updated"}
