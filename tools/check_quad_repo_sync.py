#!/usr/bin/env python3
import os, json, hashlib
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
REPOS = {
    "Hybrid": ROOT,
    "Knowledge": ROOT / "knowledge",
    "Kartel": ROOT / "vaults" / "kartel_vault",
    "Journal": ROOT / "vaults" / "journal_vault"
}

def md5sum(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def check_repo_status():
    report = {"timestamp": datetime.utcnow().isoformat(), "repos": {}}
    for name, path in REPOS.items():
        if not path.exists():
            report["repos"][name] = {"status": "❌ MISSING", "path": str(path)}
            continue
        files = list(path.rglob("*"))
        total_files = len([f for f in files if f.is_file()])
        report["repos"][name] = {
            "status": "✅ OK",
            "path": str(path),
            "files": total_files
        }
    return report

def check_reflective_integrity():
    feed_file = REPOS["Knowledge"] / "feeds" / "EURUSD_1h.json"
    journal_file = REPOS["Journal"] / "feed_sync.json"
    results = {}
    if feed_file.exists() and journal_file.exists():
        feed_hash = md5sum(feed_file)
        journal_hash = md5sum(journal_file)
        results["feed_file"] = feed_hash
        results["journal_file"] = journal_hash
        results["match"] = feed_hash == journal_hash
    else:
        results["match"] = False
    return results

if __name__ == "__main__":
    repo_status = check_repo_status()
    integrity = check_reflective_integrity()

    print("\n🧠 QUAD REPO SYNC STATUS")
    print("-" * 40)
    for name, data in repo_status["repos"].items():
        print(f"{name:<10}: {data['status']} ({data.get('files', 0)} files)")
    print("-" * 40)
    if integrity["match"]:
        print("✅ Reflective Feed–Journal hash consistent.")
    else:
        print("⚠️ Feed–Journal mismatch or missing file.")
    print(f"Timestamp: {repo_status['timestamp']}")
