"""
Reflective Risk Model Loader
----------------------------
Memuat model risiko adaptif reflektif v5.7.3r++.
"""

import json
import os
import joblib


class ReflectiveRiskModelLoader:
    def __init__(self, base_path: str = "data/model_cache"):
        self.model_path = os.path.join(base_path, "adaptive_risk_model_v573r.joblib")
        self.meta_path = os.path.join(base_path, "risk_model_meta.json")

    """
    Reflective Risk Model Loader — TUYUL FX AGI HYBRID v5.7.3r++.
    Memuat model risiko adaptif dan metadata reflektif.
    """

    from __future__ import annotations

    import json
    import os
    from typing import Any, Dict, Tuple

    import joblib


    class ReflectiveRiskModelLoader:
        def __init__(self, base_path: str = "data/model_cache"):
            self.model_path = os.path.join(base_path, "adaptive_risk_model_v573r.joblib")
            self.meta_path = os.path.join(base_path, "risk_model_meta.json")

        def load(self) -> Tuple[Any, Dict[str, Any]]:
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"❌ Model file tidak ditemukan: {self.model_path}")
            if not os.path.exists(self.meta_path):
                raise FileNotFoundError(f"❌ Metadata file tidak ditemukan: {self.meta_path}")

            model = joblib.load(self.model_path)
            with open(self.meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)

            print("────────────────────────────────────────────")
            print(f"🧠 Reflective Risk Model Loaded → {meta['model_name']} ({meta['version']})")
            print(f"Features   : {', '.join(meta.get('features', []))}")
            print(f"Coherence  : {meta.get('coherence_score', 'n/a')}")
            print(f"Protocol   : {meta.get('reflective_protocol', 'RBP v2.2')}")
            print("────────────────────────────────────────────")
            return model, meta


    __all__ = ["ReflectiveRiskModelLoader"]
