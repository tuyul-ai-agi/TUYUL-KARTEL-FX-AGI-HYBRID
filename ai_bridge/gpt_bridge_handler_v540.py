"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.2-H
GPT Bridge Handler — Reflex–Cognition–Fusion Orchestrator
"""

import os
import json
import time
from datetime import datetime
from typing import Any, Dict, Optional

import requests

from .github_api_bridge import githubCommitFile


DEFAULT_API_BASE = "http://localhost:8080/api"
OWNER = os.getenv("GITHUB_USER", "tjx578")
REPO = os.getenv("GITHUB_REPO", "TUYUL-KARTEL-FX-AGI-HYBRID")
BRANCH = "main"


class GPTBridgeHandler:
    """Handler utama GPT–AGI Hybrid Bridge"""

    def __init__(self):
        self.status = "initialized"
        self.last_sync = None
        api_base = os.getenv("AGI_API_URL", DEFAULT_API_BASE)
        self.api_base = api_base.rstrip("/")
        token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Accept": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _jit_call(
        self,
        method: str,
        endpoint: str,
        payload: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        retries: int = 3,
    ):
        path = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        url = f"{self.api_base}{path}"
        for attempt in range(retries):
            resp = requests.request(
                method,
                url,
                headers=self.headers,
                json=payload,
                params=params,
                timeout=15,
            )
            if resp.status_code in (200, 201, 204):
                return resp.json() if resp.text.strip() else {}
            print(f"⚠️ Retry {attempt + 1}: {resp.status_code} — {resp.text}")
            time.sleep(1)
        raise Exception(f"[BridgeError] {resp.status_code}: {resp.text}")

    def run_analysis(self, pair: str, timeframe: str):
        print(f"🐺 Hybrid Fusion mulai untuk {pair} ({timeframe})...")

        payload = {"pair": pair, "timeframe": timeframe}
        fusion = self._jit_call("POST", "/hybrid/runFullFusion", payload=payload)
        layer12 = self._jit_call("GET", "/hybrid/getFusionLayer12", params=payload)

        self.status = "completed"
        self.last_sync = datetime.utcnow().isoformat()

        result = {
            "pair": pair,
            "timeframe": timeframe,
            "bridge_status": self.status,
            "last_sync": self.last_sync,
            "fusion_output": layer12,
            "fusion_ack": fusion,
        }

        log_content = json.dumps(result, indent=2)
        path = f"vaults/logs/bridge_run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        githubCommitFile(OWNER, REPO, path, log_content, "🧠 Hybrid Bridge Sync", BRANCH)

        return result


if __name__ == "__main__":
    handler = GPTBridgeHandler()
    handler.run_analysis("XAUUSD", "H1")
