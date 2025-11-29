"""
GitHub API Bridge
-----------------
Interaksi AGI ↔ GitHub Actions / Repo
"""

import os
import requests


class GitHubBridge:
    def __init__(self):
        self.repo = os.getenv("GH_REPO")
        self.token = os.getenv("GITHUB_TOKEN")
        self.api_url = f"https://api.github.com/repos/{self.repo}"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
        }

    def trigger_workflow(self, workflow_name):
        url = f"{self.api_url}/actions/workflows/{workflow_name}/dispatches"
        data = {"ref": "main"}
        return requests.post(url, headers=self.headers, json=data)

    def create_issue(self, title, body):
        url = f"{self.api_url}/issues"
        data = {"title": title, "body": body}
        return requests.post(url, headers=self.headers, json=data)

    def push_file(self, path, content, message):
        url = f"{self.api_url}/contents/{path}"
        data = {
            "message": message,
            "content": content.encode("utf-8").hex(),
        }
        return requests.put(url, headers=self.headers, json=data)
