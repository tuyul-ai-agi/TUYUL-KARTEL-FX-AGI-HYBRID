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

API_BASE = os.getenv("AGI_API_URL", "http://localhost:8080/api")
OWNER = os.getenv("GITHUB_USER", "tjx578")
REPO = os.getenv("GITHUB_REPO", "TUYUL-KARTEL-FX-AGI-HYBRID")
BRANCH = "main"
TOKEN = os.getenv("GITHUB_TOKEN")


def _build_headers() -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if TOKEN:
        headers.update(
            {
                "Authorization": f"Bearer {TOKEN}",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
    return headers

class GPTBridgeHandler:
    """Handler utama GPT–AGI Hybrid Bridge"""
    def __init__(self):
        self.status = "initialized"
        self.last_sync = None

    def _jit_call(
        self, method: str, endpoint: str, payload: Optional[Dict[str, Any]] = None, retries: int = 3
    ):
        url = f"{API_BASE}{endpoint}"
        headers = _build_headers()
        for attempt in range(retries):
            try:
                kwargs: Dict[str, Any] = {"headers": headers, "timeout": 10}
                if method.upper() == "GET":
                    kwargs["params"] = payload
                else:
                    kwargs["json"] = payload

                resp = requests.request(method, url, **kwargs)
                if resp.status_code in (200, 201, 204):
                    return resp.json() if resp.text.strip() else {}
                print(f"⚠️ Retry {attempt + 1}: {resp.status_code} → {resp.text}")
            except requests.RequestException as exc:
                print(f"⚠️ Network error on attempt {attempt + 1}: {exc}")
            time.sleep(1)
        status_code = resp.status_code if "resp" in locals() else "N/A"
        error_text = resp.text if "resp" in locals() else "no response"
        raise Exception(f"[BridgeError] {status_code}: {error_text}")

    def run_analysis(self, pair: str, timeframe: str):
        print(f"🐺 Hybrid Fusion mulai untuk {pair} ({timeframe})...")

        payload = {"pair": pair, "timeframe": timeframe}

        fusion = self._jit_call("POST", "/hybrid/runFullFusion", payload)
        layer12 = self._jit_call("GET", "/hybrid/getFusionLayer12", payload)
        journal = self._jit_call("POST", "/journal/pushReasoning", payload)

        self.status = "completed"
        self.last_sync = datetime.utcnow().isoformat()

        result = {
            "pair": pair,
            "timeframe": timeframe,
            "bridge_status": self.status,
            "last_sync": self.last_sync,
            "fusion_output": layer12,
            "journal_ack": journal
        }

        # Simpan hasil refleksi ke repo
        log_content = json.dumps(result, indent=2)
        path = f"vaults/logs/bridge_run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
        githubCommitFile(OWNER, REPO, path, log_content, "🧠 Hybrid Bridge Sync", BRANCH)

        return result

    def get_status(self) -> Dict[str, Any]:
        return {
            "bridge_status": self.status,
            "status": self.status,
            "last_sync": self.last_sync,
            "api_base": API_BASE,
            "repo": f"{OWNER}/{REPO}",
        }


if __name__ == "__main__":
    handler = GPTBridgeHandler()
    handler.run_analysis("XAUUSD", "H1")
