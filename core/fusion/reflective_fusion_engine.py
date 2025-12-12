# Reflective Fusion Engine — TUYUL FX AGI HYBRID v5.7.3r++
from datetime import UTC, datetime
from typing import Dict

import numpy as np


class ReflectiveFusionEngine:
    """Layer–12 Fusion Integrator — membaca Reflex & Macro coherence."""

    def __init__(self) -> None:
        self.last_fusion_state: Dict[str, float | str] | None = None

    def integrate(self, reflex_data: Dict[str, float], macro_data: Dict[str, float]):
        conf12 = round(
            (float(reflex_data.get("conf_reflex", 0.0))
            + float(macro_data.get("conf_macro", 0.0)))
            / 2,
            3,
        )
        wlwci = round(
            float(
                np.mean(
                    [
                        float(reflex_data.get("rcadj", 0.0)),
                        float(macro_data.get("rcadj", 0.0)),
                    ]
                )
            ),
            3,
        )
        rcadj = round(
            abs(float(reflex_data.get("rcadj", 0.0)) - float(macro_data.get("rcadj", 0.0))),
            3,
        )

        reflective_state = "stable" if conf12 >= 0.9 else "adaptive"

        self.last_fusion_state = {
            "timestamp": datetime.now(UTC).isoformat(),
            "conf12": conf12,
            "wlwci": wlwci,
            "rcadj": rcadj,
            "reflective_state": reflective_state,
        }
        print(f"🧩 Reflective Fusion — CONF₁₂: {conf12}, WLWCI: {wlwci}, RCAdj: {rcadj}")
        return self.last_fusion_state
