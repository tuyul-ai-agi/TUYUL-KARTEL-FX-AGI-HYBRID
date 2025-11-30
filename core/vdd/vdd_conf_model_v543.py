"""
VDD Configuration Model v5.4.3
------------------------------
Model parameter konfigurasi VDD Hybrid — mengatur ambang batas rezim & adaptasi otomatis.
"""

import yaml

class VDDConfModel:
    def __init__(self, config_path="configs/vdd_config.yaml"):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_path) as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            self.config = {
                "thresholds": {
                    "tranquil": 0.85,
                    "stressed": 0.75,
                    "crisis": 0.6
                },
                "auto_adapt": {
                    "learning_rate": 0.05,
                    "adjust_step": 0.02
                }
            }

    def adjust_params(self, new_state: str):
        """Penyesuaian adaptif berdasarkan rezim pasar."""
        if new_state == "Stressed":
            self.config["auto_adapt"]["learning_rate"] *= 1.1
        elif new_state == "Crisis":
            self.config["auto_adapt"]["learning_rate"] *= 1.3
        elif new_state == "Tranquil":
            self.config["auto_adapt"]["learning_rate"] *= 0.95
        with open(self.config_path, "w") as f:
            yaml.dump(self.config, f)
        return self.config
