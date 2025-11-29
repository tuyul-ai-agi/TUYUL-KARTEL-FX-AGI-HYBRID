"""
API Bridge Core
---------------
Jembatan antar modul AGI Core ↔ API eksternal (Fusion / Reflex / Reflective).
"""

import requests
import os

class ApiBridgeCore:
    def __init__(self):
        self.core_api = os.getenv("HYBRID_CORE_URL", "https://api.hybridcore.tuyulkartel.ai/v1")

    def call_endpoint(self, route: str, params: dict = None):
        """Panggil endpoint internal AGI Core"""
        url = f"{self.core_api}/{route}"
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return {"error": response.text, "status_code": response.status_code}

    def send_reflex(self, pair: str, tf: str):
        return self.call_endpoint("reflex/analyze", {"pair": pair, "timeframe": tf})

    def send_fusion(self, conf12: float, wlwci: float):
        return self.call_endpoint("fusion", {"reflex_conf": conf12, "fusion_conf": wlwci, "wlwci": wlwci})

    def sync_vaults(self):
        return self.call_endpoint("vault/sync")
