from __future__ import annotations

"""Reflective API Loader for TUYUL FX AGI HYBRID."""

from .api_router import ReflectiveAPIRouter  # noqa: F401
from .client_agi_hybrid import AgiHybridClient as AGIHybridClient

__version__ = "v5.7.3r++"
__protocol__ = "RBP v2.2"

__all__ = ["ReflectiveAPIRouter", "AGIHybridClient"]

print("🌐 Reflective API Layer Initialized — TUYUL v5.7.3r++")

