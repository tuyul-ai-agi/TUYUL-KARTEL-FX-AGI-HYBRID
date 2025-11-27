"""
🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.1-H
AI Bridge Package (Hybrid Edition)
Menghubungkan GPT Layer dengan sistem AGI Hybrid internal & GitHub Bridge.
"""

import os
from .gpt_bridge_handler_v540 import GPTBridgeHandler
from .github_api_bridge import getRepoContents, githubCommitFile, checkRepoAccess

__all__ = ["GPTBridgeHandler", "getRepoContents", "githubCommitFile", "checkRepoAccess"]
__version__ = "5.4.1-H"
__author__ = "TUYUL LAB 🧠⚡"

# === Hybrid Bridge Meta Config ===
AGI_BRIDGE_CONFIG = {
    "version": __version__,
    "connected_repo": os.getenv("GITHUB_REPO", "TUYUL-KARTEL-FX-AGI-HYBRID"),
    "owner": os.getenv("GITHUB_USER", "tjx578"),
    "status": "active",
    "bridge_mode": "hybrid-reflective",
    "description": "Fusion link between GPT reasoning layer and AGI GitHub Vault",
}
