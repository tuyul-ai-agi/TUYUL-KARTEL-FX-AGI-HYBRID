"""
Sync Hybrid Repo
----------------
Sinkronisasi repo utama ke GitHub Vault (AGI Core & Journal).
"""

from ai_bridge.github_api_bridge import GitHubBridge

if __name__ == "__main__":
    bridge = GitHubBridge()
    bridge.sync_repo(branch="main")
    print("✅ Hybrid Repo Synced Successfully.")
