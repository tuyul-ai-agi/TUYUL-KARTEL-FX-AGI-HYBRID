# ApiBridgeCore — Reflective API Bridge v5.7.3r++
import datetime
import json

import requests


class ApiBridgeCore:
    """Jembatan utama komunikasi API antara AGI Hybrid dan endpoint eksternal"""

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        self.last_sync = None
        self.integrity_index = 0.0

    def post(self, endpoint: str, payload: dict):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, headers=self.headers, json=payload, timeout=5)
        self._reflect(response)
        return response.json() if response.ok else {"error": response.status_code}

    def get(self, endpoint: str):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, headers=self.headers, timeout=5)
        self._reflect(response)
        return response.json() if response.ok else {"error": response.status_code}

    def _reflect(self, response):
        """Evaluasi reflektif setiap komunikasi API"""

        self.last_sync = datetime.datetime.utcnow().isoformat() + "Z"
        latency = response.elapsed.total_seconds() * 1000
        self.integrity_index = round(max(0.9, 1 - (latency / 2000)), 3)
        print(
            f"🌐 API Bridge Reflective — Integrity: {self.integrity_index}, Latency: {latency:.1f} ms"
        )
