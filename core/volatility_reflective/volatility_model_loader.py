"""
Reflective Volatility Model Loader
----------------------------------
Memuat model VDD (Volatility–Deviation–Distribution) reflektif v5.7.3r++.
"""

import json
import os
import joblib


class ReflectiveVolatilityModelLoader:
    def __init__(self, base_path: str = "data/model_cache"):
        self.model_path = os.path.join(base_path, "reflective_volatility_model_v573r.joblib")
        self.meta_path = os.path.join(base_path, "vdd_model_meta.json")

    def load(self):
        """Memuat model volatilitas reflektif dan metadata-nya."""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"❌ Model file tidak ditemukan: {self.model_path}")
        if not os.path.exists(self.meta_path):
            raise FileNotFoundError(f"❌ Metadata file tidak ditemukan: {self.meta_path}")

        model = joblib.load(self.model_path)
        with open(self.meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        print("────────────────────────────────────────────")
        print(f"🌫️ Reflective Volatility Model Loaded → {meta['model_name']} ({meta['version']})")
        print(f"Features   : {', '.join(meta['features'])}")
        print(f"Coherence  : {meta.get('coherence_index', 'n/a')}")
        print(f"Protocol   : {meta.get('reflective_protocol', 'n/a')}")
        print("────────────────────────────────────────────")
        return model, meta


__all__ = ["ReflectiveVolatilityModelLoader"]
