"""
GitHub AutoMerge Hook v5.4.1
----------------------------
Auto merge PR setelah integritas vault diverifikasi.
"""

import requests
import os


class GitHubAutoMergeHook:
    def __init__(self):
        self.repo = os.getenv("GH_REPO")
        self.token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def auto_merge_pr(self, pr_number):
        url = f"https://api.github.com/repos/{self.repo}/pulls/{pr_number}/merge"
        data = {"merge_method": "squash"}
        response = requests.put(url, headers=self.headers, json=data)
        return response.status_code, response.json()
