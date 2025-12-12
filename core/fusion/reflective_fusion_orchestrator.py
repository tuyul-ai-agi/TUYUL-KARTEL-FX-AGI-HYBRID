# Reflective Fusion Orchestrator — TUYUL FX AGI HYBRID v5.7.3r++
from datetime import UTC, datetime
from typing import Dict

from .fusion_confidence_core import FusionConfidenceCore
from .reflective_fusion_engine import ReflectiveFusionEngine


class ReflectiveFusionOrchestrator:
    """Orkestrator Layer–12 — menggabungkan semua hasil fusion & coherence."""

    def __init__(self) -> None:
        self.conf_core = FusionConfidenceCore()
        self.engine = ReflectiveFusionEngine()

    def run_fusion_cycle(self, reflex_data: Dict[str, float], macro_data: Dict[str, float]):
        """Integrasi lintas layer."""

        result = self.engine.integrate(reflex_data, macro_data)
        metrics = self.conf_core.compute([result["conf12"], result["wlwci"], result["rcadj"]])
        final_conf = {
            "timestamp": datetime.now(UTC).isoformat(),
            "fusion_confidence": metrics["conf12"],
            "wlwci": metrics["wlwci"],
            "rcadj": metrics["rcadj"],
            "reflective_state": metrics["reflective_state"],
        }
        print(f"⚙️ Fusion Orchestrator — Reflective State: {final_conf['reflective_state']}")
        return final_conf
