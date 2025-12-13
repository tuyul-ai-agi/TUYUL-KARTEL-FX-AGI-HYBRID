"""
VDD Regime Model
----------------
Menentukan state rezim berdasarkan fitur dan ambang batas dari konfigurasi.
"""

import yaml


class VDDRegimeModel:
    def __init__(self, config_path="modules/vdd_hybrid/vdd_config.yaml"):
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
        self.thresholds = cfg["thresholds"]

    def classify(self, features: dict):
        coh = features["coherence_index"]
        if coh > self.thresholds["tranquil"]:
            return "Tranquil"
        elif coh > self.thresholds["stressed"]:
            return "Stressed"
        else:
            return "Crisis"
