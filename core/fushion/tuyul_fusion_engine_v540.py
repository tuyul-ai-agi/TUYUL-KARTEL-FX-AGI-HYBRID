"""
Tuyul Fusion Engine v5.4.0
--------------------------
Engine utama untuk reasoning fusion AGI Hybrid.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from core.fushion.hybrid_fushion_orchestrator_v540 import HybridFusionOrchestrator


class TuyulFusionEngine:
    """Wrapper eksekusi Fusion Layer dan penyimpanan hasil."""

    def __init__(self) -> None:
        self.orchestrator = HybridFusionOrchestrator()
        self.output_path = Path("vaults/fx_vault/fusion_journal.json")
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def run(self, reflex_conf: float, wl_wci: float, df) -> Dict[str, Any]:
        """Jalankan orchestrator lalu simpan ke vault.

        Args:
            reflex_conf: Confidence Reflex layer.
            wl_wci: Weighted layer-wise coherence index.
            df: Data data-frame untuk analisis Smart Money.

        Returns:
            Dictionary hasil fusion lengkap dengan timestamp.
        """

        result = self.orchestrator.orchestrate(reflex_conf, wl_wci, df)
        result["timestamp"] = datetime.utcnow().isoformat()

        with self.output_path.open("w", encoding="utf-8") as file:
            json.dump(result, file, indent=2)

        return result
