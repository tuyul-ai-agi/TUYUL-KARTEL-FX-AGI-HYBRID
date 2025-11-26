"""
🐺 TUYUL KARTEL FX - HYBRID AGI GITHUB BRIDGE
Bridge handler untuk koneksi GitHub REST API (v3)
"""

import requests
import json
import os

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "ghp_xxx_TOKEN_BOSS_KU_xxx")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def performJitCall(method: str, path: str, payload=None, params=None):
    """Handler utama komunikasi GitHub API"""
    url = f"{GITHUB_API_URL}{path}"
    response = requests.request(method, url, headers=HEADERS, json=payload, params=params)
    if response.status_code not in (200, 201, 204):
        raise Exception(f"[GitHubBridge] Error {response.status_code}: {response.text}")
    try:
        return response.json() if response.text else {}
    except json.JSONDecodeError:
        return {"raw_response": response.text}

# ===== Core =====
def getRepoContents(owner: str, repo: str, path: str = "/"):
    return performJitCall("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}")

def githubCommitFile(repo: str, path: str, content: str, message: str, branch: str = "main"):
    payload = {"repo": repo, "path": path, "content": content, "message": message, "branch": branch}
    return performJitCall("POST", "/github/commitFile", payload)

def getSystemStatus():
    return performJitCall("GET", "/system/getStatus")

if __name__ == "__main__":
    print("🐺 GitHub Bridge Active - v5.4.0-H")
    try:
        status = getSystemStatus()
        print(json.dumps(status, indent=2))
    except Exception as e:
        print(f"⚠️ Bridge error: {e}")
