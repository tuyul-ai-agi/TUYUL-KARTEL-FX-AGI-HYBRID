"""
Reflective Reasoner v5.4.0
--------------------------
Analisa reflektif AGI terhadap hasil reasoning fusion.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class ReflectiveReasoner:
    """Menilai bias dan integritas hasil fusion."""

    def __init__(self, output_path: Path | str = "vaults/journal_vault/reflection_output.json") -> None:
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def evaluate(self, fusion_result: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluasi hasil fusion untuk bias dan integritas."""

        bias_delta = abs(fusion_result["RCAdj"] - fusion_result["CONF12"])
        integrity_index = round((fusion_result["CONF12"] + fusion_result["RCAdj"]) / 2, 3)
        result = {
            "BiasDelta": round(bias_delta, 3),
            "IntegrityIndex": integrity_index,
            "Reflection": "Stable" if integrity_index > 0.85 else "Need Relearn",
        }
        with self.output_path.open("w", encoding="utf-8") as file:
            json.dump(result, file, indent=2)
        return result
