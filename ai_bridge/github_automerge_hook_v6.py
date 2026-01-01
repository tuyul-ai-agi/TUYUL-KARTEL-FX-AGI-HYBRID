"""
GitHub AutoMerge Hook v6.0
-----------------------------------------
Automatically merges PRs when reflective checks (coherence, integrity)
meet the minimum reflective thresholds.
"""

import os
import requests


class AutoMergeHook:
    def __init__(self, token: str | None = None, repo: str | None = None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        if not self.token:
            raise RuntimeError("GITHUB_TOKEN is required for AutoMergeHook")
        self.repo = repo or os.getenv("GITHUB_REPOSITORY", "tuyul-ai-agi/TUYUL-KARTEL-FX-AGI-HYBRID")

    def auto_merge(self, pr_number: int, coherence: float, integrity: float):
        if coherence <= 0.92 or integrity <= 0.93:
            print(f"PR #{pr_number} held (Coherence={coherence}, Integrity={integrity})")
            return False

        url = f"https://api.github.com/repos/{self.repo}/pulls/{pr_number}/merge"
        headers = {"Authorization": f"token {self.token}", "Accept": "application/vnd.github+json"}
        data = {"merge_method": "squash"}
        response = requests.put(url, headers=headers, json=data, timeout=20)
        if response.status_code == 200:
            print(f"PR #{pr_number} merged reflectively (Coherence={coherence}, Integrity={integrity})")
            return True

        print(f"PR #{pr_number} merge failed (status={response.status_code}): {response.text}")
        return False
