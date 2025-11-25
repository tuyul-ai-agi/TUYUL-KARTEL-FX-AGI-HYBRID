"""TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0 OpenAPI bridge module."""

from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.tuyulfx.ai/v5.4.0"
JsonDict = Dict[str, Any]


class TuyulBridge:
    """HTTP client for TUYUL FX AGI Hybrid OpenAPI endpoints."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    # ====== FUSION LAYER 12 ======
    def fusion_analyze(self, pair: str, timeframe: str) -> JsonDict:
        return self._post("/fusion/analyze", {"pair": pair, "timeframe": timeframe})

    def fusion_confidence(self) -> JsonDict:
        return self._get("/fusion/confidence")

    def fusion_wlwci(self) -> JsonDict:
        return self._get("/fusion/wlwci")

    def fusion_montecarlo(self, pair: str) -> JsonDict:
        return self._post("/fusion/montecarlo", {"pair": pair})

    def fusion_save_journal(self, payload: JsonDict) -> JsonDict:
        return self._post("/fusion/save-journal", payload)

    # ====== REFLEX ENGINE ======
    def reflex_analyze(self, pair: str) -> JsonDict:
        return self._post("/reflex/analyze", {"pair": pair})

    def reflex_status(self) -> JsonDict:
        return self._get("/reflex/status")

    def reflex_logs(self) -> JsonDict:
        return self._get("/reflex/logs")

    # ====== RISK ENGINE ======
    def risk_calculate(self, balance: float, sl_pips: float, pair: str) -> JsonDict:
        payload = {"balance": balance, "sl_pips": sl_pips, "pair": pair}
        return self._post("/risk/calculate", payload)

    def risk_summary(self) -> JsonDict:
        return self._get("/risk/summary")

    def risk_policy(self) -> JsonDict:
        return self._get("/risk/policy")

    # ====== VAULT SYNC ======
    def vault_sync(self) -> JsonDict:
        return self._post("/vault/sync", {})

    def vault_status(self) -> JsonDict:
        return self._get("/vault/status")

    # ====== REFLECTIVE CYCLE ======
    def reflective_trigger(self) -> JsonDict:
        return self._post("/reflective/trigger", {})

    def reflective_report(self) -> JsonDict:
        return self._get("/reflective/report")

    # ====== GPT BRIDGE ======
    def gpt_bridge(self, payload: JsonDict) -> JsonDict:
        return self._post("/gpt/bridge", payload)

    # ====== SYSTEM ======
    def system_status(self) -> JsonDict:
        return self._get("/system/status")

    # ====== HTTP HANDLERS ======
    def _get(self, path: str) -> JsonDict:
        return self._request("get", path)

    def _post(self, path: str, data: JsonDict) -> JsonDict:
        return self._request("post", path, json=data)

    def _request(self, method: str, path: str, **kwargs: Any) -> JsonDict:
        url = f"{BASE_URL}{path}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
