"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.2-H
GPT Bridge Handler — Reflex–Cognition–Fusion Orchestrator
"""

import os
import json
import time
import requests
from datetime import datetime
from .github_api_bridge import githubCommitFile

API_BASE = os.getenv("AGI_API_URL", "https://api.github.com")
OWNER = os.getenv("GITHUB_USER", "tjx578")
REPO = os.getenv("GITHUB_REPO", "TUYUL-KARTEL-FX-AGI-HYBRID")
BRANCH = "main"
TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

class GPTBridgeHandler:
    """Handler utama GPT–AGI Hybrid Bridge"""
    def __init__(self):
        self.status = "initialized"
        self.last_sync = None

    def _jit_call(self, method: str, endpoint: str, payload=None, retries=3):
        url = f"{API_BASE}{endpoint}"
        for attempt in range(retries):
            resp = requests.request(method, url, headers=HEADERS, json=payload)
            if resp.status_code in (200, 201, 204):
                return resp.json() if resp.text.strip() else {}
            print(f"⚠️ Retry {attempt+1}: {resp.status_code}")
            time.sleep(1)
        raise Exception(f"[BridgeError] {resp.status_code}: {resp.text}")

    def run_analysis(self, pair: str, timeframe: str):
        print(f"🐺 Hybrid Fusion mulai untuk {pair} ({timeframe})...")

        fusion = self._jit_call("POST", "/hybrid/runFullFusion")
        layer12 = self._jit_call("GET", "/hybrid/getFusionLayer12")
        journal = self._jit_call("POST", "/journal/pushReasoning")

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


if __name__ == "__main__":
    handler = GPTBridgeHandler()
    handler.run_analysis("XAUUSD", "H1")
