#!/usr/bin/env python3
"""Hybrid repo synchronization helper using WOLF_KEY fallback."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Tuple

import requests

DEFAULT_REPO = "tjx578/TUYUL-KARTEL-FX-AGI-HYBRID"
DEFAULT_BRANCH = "main"
SNAPSHOT_DIR = Path("vaults")


def ensure_token() -> Tuple[str, str]:
    """Return a GitHub token, preferring ``GITHUB_TOKEN`` then ``WOLF_KEY``.

    The selected token is also exported back to ``GITHUB_TOKEN`` so subprocesses
    inherit the credential during subsequent sync steps.
    """

    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        return github_token, "GITHUB_TOKEN"

    wolf_key = os.getenv("WOLF_KEY")
    if not wolf_key:
        raise RuntimeError(
            "WOLF_KEY is not available and no GITHUB_TOKEN is set; cannot authenticate."
        )

    os.environ["GITHUB_TOKEN"] = wolf_key
    return wolf_key, "WOLF_KEY"


def build_session(token: str) -> requests.Session:
    """Create a GitHub-authenticated HTTP session."""

    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "tuyul-hybrid-sync/1.0",
        }
    )
    return session


def fetch_branch_sha(session: requests.Session, repo: str, branch: str) -> str:
    """Fetch the latest commit SHA for a branch."""

    branch_url = f"https://api.github.com/repos/{repo}/branches/{branch}"
    response = session.get(branch_url, timeout=15)
    response.raise_for_status()
    return response.json()["commit"]["sha"]


def download_snapshot(session: requests.Session, repo: str, ref: str) -> Path:
    """Download a tarball snapshot for the requested ref."""

    snapshot_name = f"{repo.replace('/', '_')}-{ref[:7]}.tar.gz"
    snapshot_path = SNAPSHOT_DIR / snapshot_name
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)

    url = f"https://api.github.com/repos/{repo}/tarball/{ref}"
    with session.get(url, stream=True, timeout=30) as response:
        response.raise_for_status()
        with snapshot_path.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    handle.write(chunk)

    return snapshot_path


def sync_hybrid_repo(repo: str, branch: str) -> Path:
    """Sync the remote repository snapshot into the local vaults directory."""

    token, source = ensure_token()
    session = build_session(token)

    print(f"🔐 Using {source} for GitHub authentication")
    print(f"🔁 Syncing repo: {repo} @ {branch}")

    head_sha = fetch_branch_sha(session, repo, branch)
    snapshot_path = download_snapshot(session, repo, head_sha)

    print(f"✅ Latest commit: {head_sha}")
    print(f"💾 Snapshot saved to: {snapshot_path}")
    print("🧠 Fusion layer can reload from the refreshed snapshot now.")

    return snapshot_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync TUYUL Hybrid repo using WOLF_KEY/GITHUB_TOKEN authentication."
    )
    parser.add_argument(
        "--repo",
        default=DEFAULT_REPO,
        help=f"GitHub repo in owner/name format (default: {DEFAULT_REPO})",
    )
    parser.add_argument(
        "--branch",
        default=DEFAULT_BRANCH,
        help=f"Branch or ref to sync (default: {DEFAULT_BRANCH})",
    )
    args = parser.parse_args()

    try:
        sync_hybrid_repo(args.repo, args.branch)
    except Exception as exc:  # noqa: BLE001
        print(f"❌ Sync failed: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
