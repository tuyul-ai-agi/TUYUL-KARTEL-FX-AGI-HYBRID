"""
🐺 TUYUL KARTEL FX - HYBRID AGI GITHUB BRIDGE v5.4.1-H (Final)
Bridge handler resmi untuk koneksi dua arah GitHub REST API (v3)
Didesain untuk integrasi dengan TUYUL HYBRID AGI dan workflow GitHub Actions.
"""

import base64
import json
import os
import time

import requests

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Token diambil dari environment variable GitHub Action


def _build_headers(require_auth: bool = True) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    elif require_auth:
        raise EnvironmentError("GITHUB_TOKEN is required for authenticated GitHub API calls")
    return headers


def performJitCall(
    method: str,
    path: str,
    payload=None,
    params=None,
    retries: int = 3,
    delay: float = 1.5,
    require_auth: bool = True,
):
    """Handler utama komunikasi GitHub API dengan retry logic dan error handling"""
    url = f"{GITHUB_API_URL}{path}"
    for attempt in range(retries):
        try:
            response = requests.request(
                method,
                url,
                headers=_build_headers(require_auth=require_auth),
                json=payload,
                params=params,
            )
            if response.status_code in (200, 201, 204):
                try:
                    return response.json() if response.text else {}
                except json.JSONDecodeError:
                    return {"raw_response": response.text}
            else:
                print(f"[GitHubBridge] ⚠️ Attempt {attempt + 1} failed: {response.status_code} - {response.text}")
                time.sleep(delay)
        except requests.exceptions.RequestException as e:
            print(f"[GitHubBridge] Network error: {e}")
            time.sleep(delay)
    raise Exception(f"[GitHubBridge] ❌ Failed after {retries} attempts at {url}")

# ===== Core GitHub Bridge Functions =====
def getRepoContents(owner: str, repo: str, path: str = "/"):
    """Ambil isi direktori atau file dari repo GitHub"""
    return performJitCall("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}", require_auth=False)

def githubCommitFile(owner: str, repo: str, path: str, content: str, message: str, branch: str = "main"):
    """Upload atau update file ke repo GitHub secara aman"""
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": message,
        "content": encoded_content,
        "branch": branch
    }
    return performJitCall("PUT", f"/repos/{owner}/{repo}/contents/{path}", payload)

def checkRepoAccess(owner: str, repo: str):
    """Verifikasi hak akses token ke repo tertentu"""
    try:
        result = performJitCall("GET", f"/repos/{owner}/{repo}")
        return {
            "full_name": result.get("full_name"),
            "permissions": result.get("permissions", {}),
            "default_branch": result.get("default_branch")
        }
    except Exception as e:
        return {"error": str(e)}

def getSystemStatus():
    """Ambil status sistem GitHub global (uptime / incident)"""
    try:
        response = requests.get("https://www.githubstatus.com/api/v2/status.json", timeout=10)
        data = response.json()
        return {"github_status": data.get("status", {}).get("description", "unknown")}
    except Exception as e:
        return {"error": str(e)}

def bridgeDiagnostics(owner: str, repo: str):
    """Menjalankan diagnosa penuh koneksi bridge dan token"""
    print("\n🐺 Wolf GitHub Bridge Diagnostics...")
    print(json.dumps(getSystemStatus(), indent=2))
    access_info = checkRepoAccess(owner, repo)
    print(json.dumps(access_info, indent=2))
    if "error" not in access_info:
        print(f"✅ Akses valid ke repo: {access_info.get('full_name')}")
    else:
        print(f"⚠️ Tidak dapat mengakses repo: {access_info['error']}")

if __name__ == "__main__":
    print("🐺 GitHub Bridge Online - v5.4.1-H")
    OWNER = os.getenv("GITHUB_USER", "tjx578")
    REPO = os.getenv("GITHUB_REPO", "TUYUL-KARTEL-FX-AGI-HYBRID")
    bridgeDiagnostics(OWNER, REPO)
