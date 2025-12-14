"""
GPT Bridge Handler v5.7.3r++
----------------------------
Menghubungkan GPT Reasoning ↔ Fusion–Reflective Engine.
"""
import json
import os
from datetime import datetime
from modules.montecarlo_engine_v22 import simulate_price_paths


class GPTBridgeHandler:
    def __init__(self):
        self.version = "v5.7.3r++"

    def process_signal(self, message: str, prices: list[float]):
        if not prices:
            raise ValueError("prices must be a non-empty list")

        mc_result = simulate_price_paths(prices)
        response = {
            "message": message,
            "reflection": "Reflex–Fusion–Reflective processed",
            "montecarlo": mc_result,
            "bridge_version": "RBP v2.2",
            "timestamp": datetime.utcnow().isoformat()
        }
        os.makedirs("logs", exist_ok=True)
        with open("logs/gpt_bridge.log", "a", encoding="utf-8") as f:
            f.write(json.dumps(response) + "\n")
        return response
