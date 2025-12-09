"""
GitHub AutoMerge Hook v5.7.3r++
-------------------------------
Menggabungkan pull request reflektif setelah Quad Repo Sync sukses.
"""

import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("REPO", "Hybrid")
API_BASE = f"https://api.github.com/repos/TUYUL-LABS/{REPO}/pulls"


def automerge_reflective_pr():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    prs = requests.get(API_BASE, headers=headers).json()
    for pr in prs:
        if "[REFLECTIVE SYNC]" in pr["title"]:
            merge_url = f"{API_BASE}/{pr['number']}/merge"
            requests.put(merge_url, headers=headers, json={"merge_method": "squash"})
            print(f"[MERGE] Reflective PR merged: {pr['title']}")
    print("[DONE] AutoMerge Hook completed ✅")


if __name__ == "__main__":
    automerge_reflective_pr()
