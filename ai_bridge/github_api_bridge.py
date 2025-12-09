"""
GitHub API Bridge v5.7.3r++
---------------------------
Sinkronisasi Quad Repo (Hybrid–Knowledge–Kartel–Journal)
melalui GitHub REST API secara reflektif (RBP v2.2).
"""

import os
import requests
from datetime import datetime

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPOS = ["Hybrid", "Knowledge", "Kartel", "Journal"]
API_URL = "https://api.github.com/repos/TUYUL-LABS/{repo}/actions/workflows/quad_vault_reflective_sync.yml/dispatches"


def trigger_workflow(repo: str):
    url = API_URL.format(repo=repo)
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    data = {"ref": "main"}
    res = requests.post(url, headers=headers, json=data, timeout=15)
    print(f"[API] Triggered reflective sync on {repo}: {res.status_code}")
    return res.status_code == 204


def sync_all():
    print("[SYNC] Starting Quad Repo Reflective Sync @", datetime.utcnow().isoformat())
    for repo in REPOS:
        trigger_workflow(repo)
    print("[DONE] Quad Repo Reflective Sync Completed ✅")


if __name__ == "__main__":
    sync_all()
