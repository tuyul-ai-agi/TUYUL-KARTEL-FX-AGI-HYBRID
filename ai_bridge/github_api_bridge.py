"""
GitHub API Bridge v6.0
-----------------------------------------
Connects reflective reasoning layer with GitHub Actions and repositories.
Used by reflective_agent_executor to write awareness logs or issues.
"""

import os
from typing import Tuple
import requests


class GitHubBridge:
    def __init__(self, token: str | None = None, repo: str | None = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise RuntimeError("GITHUB_TOKEN is required for GitHubBridge")
        self.repo = repo or os.getenv("GITHUB_REPOSITORY", "tuyul-ai-agi/TUYUL-KARTEL-FX-AGI-HYBRID")

    def _headers(self) -> dict:
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json",
        }

    def create_issue(self, title: str, body: str) -> Tuple[int, dict]:
        url = f"https://api.github.com/repos/{self.repo}/issues"
        payload = {"title": title, "body": body}
        response = requests.post(url, headers=self._headers(), json=payload, timeout=20)
        return response.status_code, response.json() if response.text else {}

    def dispatch_workflow(self, workflow: str, ref: str = "main", inputs: dict | None = None) -> int:
        url = f"https://api.github.com/repos/{self.repo}/actions/workflows/{workflow}/dispatches"
        payload = {"ref": ref, "inputs": inputs or {}}
        response = requests.post(url, headers=self._headers(), json=payload, timeout=20)
        return response.status_code"""
GitHub API Bridge v5.7.3r++
---------------------------
Sinkronisasi Quad Repo (Hybrid–Knowledge–Kartel–Journal)
melalui GitHub REST API secara reflektif (RBP v2.2).
"""

import os
from datetime import datetime
from typing import Iterable

import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPOS = ["Hybrid", "Knowledge", "Kartel", "Journal"]
API_URL = "https://api.github.com/repos/TUYUL-LABS/{repo}/actions/workflows/quad_vault_reflective_sync.yml/dispatches"


def _build_headers() -> dict:
    if not GITHUB_TOKEN:
        raise RuntimeError("GITHUB_TOKEN is not set; cannot trigger workflows")
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }


def trigger_workflow(repo: str) -> bool:
    url = API_URL.format(repo=repo)
    try:
        res = requests.post(
            url,
            headers=_build_headers(),
            json={"ref": "main"},
            timeout=15,
        )
        if res.status_code == 204:
            print(f"[API] Reflective sync triggered for {repo}")
            return True

        print(
            f"[API] Failed to trigger {repo} (status={res.status_code}): {res.text}"
        )
        return False
    except requests.RequestException as exc:
        print(f"[API] Exception while triggering {repo}: {exc}")
        return False


def sync_all(repos: Iterable[str] = None) -> bool:
    repos = list(repos) if repos is not None else REPOS
    print("[SYNC] Starting Quad Repo Reflective Sync @", datetime.utcnow().isoformat())
    results = [trigger_workflow(repo) for repo in repos]
    success = all(results)
    status_text = "✅ Completed" if success else "⚠️ Completed with errors"
    print(f"[DONE] {status_text}")
    return success


if __name__ == "__main__":
    sync_all()
