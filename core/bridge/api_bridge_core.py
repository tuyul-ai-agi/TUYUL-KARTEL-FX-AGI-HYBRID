"""
API Bridge Core
---------------
Jembatan antar modul AGI Core ↔ API eksternal (Fusion / Reflex / Reflective).
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


class ApiBridgeCore:
    """Penghubung ke endpoint internal AGI Core."""

    def __init__(self) -> None:
        self.core_api = os.getenv("HYBRID_CORE_URL", "https://api.hybridcore.tuyulkartel.ai/v1")

    def call_endpoint(self, route: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Panggil endpoint internal AGI Core."""

        url = f"{self.core_api}/{route}"
        response = requests.get(url, params=params, timeout=15)
        if response.status_code == 200:
            return response.json()
        return {"error": response.text, "status_code": response.status_code}

    def send_reflex(self, pair: str, tf: str) -> Dict[str, Any]:
        """Kirim permintaan analisis Reflex."""

        return self.call_endpoint("reflex/analyze", {"pair": pair, "timeframe": tf})

    def send_fusion(self, conf12: float, wlwci: float) -> Dict[str, Any]:
        """Kirim data fusion menuju endpoint Fusion layer."""

        return self.call_endpoint(
            "fusion", {"reflex_conf": conf12, "fusion_conf": wlwci, "wlwci": wlwci}
        )

    def sync_vaults(self) -> Dict[str, Any]:
        """Trigger sinkronisasi vault."""

        return self.call_endpoint("vault/sync")

