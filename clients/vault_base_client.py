"""
Vault Base Client
-----------------
Kelas dasar untuk komunikasi HTTP antar Vault AGI Hybrid.
Menangani autentikasi, headers, dan koneksi API standar.
"""

import requests
import os
import time

class VaultBaseClient:
    def __init__(self, base_url: str, api_key_env: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = os.getenv(api_key_env, "")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "TuyulKartel-FX-AGI/5.4.4"
        }

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        retries = 3
        for attempt in range(retries):
            try:
                response = requests.request(method, url, headers=self.headers, timeout=10, **kwargs)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                if attempt < retries - 1:
                    time.sleep(1.5)
                else:
                    raise e

    def get(self, endpoint: str, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, data=None, json=None):
        return self._request("POST", endpoint, json=json or data)

    def ping(self):
        """Tes koneksi ke Vault"""
        try:
            r = self.get("status")
            return {"status": "connected", "response": r}
        except Exception as e:
            return {"status": "error", "error": str(e)}
