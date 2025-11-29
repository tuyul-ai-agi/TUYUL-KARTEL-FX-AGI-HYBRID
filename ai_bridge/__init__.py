"""
ai_bridge package
-----------------
Lapisan integrasi antara AGI Hybrid (Reflex–Fusion–Reflective) dengan GPT, Vault, dan GitHub API.

Version: v5.4.4-TriVault
"""

__version__ = "5.4.4"
__author__ = "Tuyul Kartel FX Hybrid Team"

from .gpt_bridge_handler_v540 import GPTBridge
from .gpt_command_parser_v540 import CommandParser
from .gpt_context_memory import ContextMemory
from .github_api_bridge import GitHubBridge
from .vault_autosync_v541 import VaultAutoSync
from .bridge_observer_v543 import BridgeObserver

__all__ = [
    "GPTBridge",
    "CommandParser",
    "ContextMemory",
    "GitHubBridge",
    "VaultAutoSync",
    "BridgeObserver",
]
