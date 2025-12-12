# ============================================================
# 🧠 TUYUL FX AGI v5.8.2-HYBRID
# File: /core/api/client_agi_hybrid.py
# ------------------------------------------------------------
# Client resmi untuk komunikasi ke AGI Hybrid Core API.
# Menyediakan akses endpoint: /fusion/analyze, /vault/sync,
# /risk/calculate, dan /reflective/cycle.
# ============================================================

import os
import httpx
from datetime import datetime
from typing import Optional, Dict, Any


class AgiHybridClient:
    """
    Client API utama untuk berinteraksi dengan AGI Hybrid Core TUYUL-KARTEL-FX.
    """

    def __init__(self, base_url: Optional[str] = None, token: Optional[str] = None):
        self.base_url = base_url or os.getenv("HYBRID_API_URL", "https://api.hybridcore.tuyulkartel.ai/v1")
        self.token = token or os.getenv("HYBRID_API_TOKEN", "")
        self.session = httpx.Client(timeout=30)

    # ------------------------------------------------------------
    # 🔹 Header Authorization
    # ------------------------------------------------------------
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "User-Agent": "TUYUL-HYBRID-CLIENT-v5.8.2",
        }

    # ------------------------------------------------------------
    # 🔹 Endpoint: Fusion Analysis
    # ------------------------------------------------------------
    def fusion_analyze(self, pair: str, timeframe: str, twms_payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/fusion/analyze"
        payload = {
            "pair": pair,
            "timeframe": timeframe,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "twms": twms_payload,
        }
        response = self.session.post(url, headers=self._headers(), json=payload)
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------
    # 🔹 Endpoint: Vault Sync (Reflective Journal)
    # ------------------------------------------------------------
    def vault_sync(self) -> Dict[str, Any]:
        url = f"{self.base_url}/vault/sync"
        response = self.session.post(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------
    # 🔹 Endpoint: Risk Calculation
    # ------------------------------------------------------------
    def risk_calculate(self, pair: str, balance: float, sl_pips: int) -> Dict[str, Any]:
        url = f"{self.base_url}/risk/calculate"
        payload = {"pair": pair, "balance": balance, "sl_pips": sl_pips}
        response = self.session.post(url, headers=self._headers(), json=payload)
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------
    # 🔹 Endpoint: Reflective Cycle
    # -----------------
