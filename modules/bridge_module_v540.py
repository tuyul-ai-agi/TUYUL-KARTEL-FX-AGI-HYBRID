import aiohttp
import asyncio
import json
import time
from datetime import datetime


class TuyulAgiBridgeV540:
    def __init__(self, base_url="https://api.tuyulfx.ai/v5.4.0", api_key=None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = None
        self.request_count = 0

    async def _ensure_session(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def _request(self, method, path, payload=None, retries=3):
        await self._ensure_session()
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        for attempt in range(1, retries + 1):
            start_time = time.time()
            try:
                async with self.session.request(method, url, headers=headers, json=payload, timeout=20) as resp:
                    latency = round((time.time() - start_time) * 1000, 2)
                    data = await resp.json(content_type=None)
                    return {
                        "status": "ok",
                        "endpoint": path,
                        "data": data,
                        "latency_ms": latency,
                        "timestamp": datetime.utcnow().isoformat(),
                    }
            except Exception as e:
                if attempt == retries:
                    return {"error": True, "message": str(e), "endpoint": path, "retries": retries}
                await asyncio.sleep(1.5 * attempt)

    async def close(self):
        if self.session:
            await self.session.close()

    # ----------------------------- FUSION LAYER -----------------------------

    async def fusion_analyze(self, pair: str, timeframe: str):
        result = await self._request("POST", "/fusion/analyze", {"pair": pair, "timeframe": timeframe})
        if result.get("status") == "ok":
            await self.reflective_trigger()  # Auto trigger reflective learning
        return result

    async def fusion_confidence(self):
        return await self._request("GET", "/fusion/confidence")

    async def fusion_wlwci(self):
        return await self._request("GET", "/fusion/wlwci")

    async def fusion_coherence_map(self):
        return await self._request("GET", "/fusion/coherence-map")

    async def fusion_montecarlo(self, pair: str):
        return await self._request("POST", "/fusion/montecarlo", {"pair": pair})

    async def fusion_save_journal(self, data: dict):
        return await self._request("POST", "/fusion/save-journal", data)

    # ----------------------------- REFLEX LAYER -----------------------------

    async def reflex_analyze(self, pair: str):
        return await self._request("POST", "/reflex/analyze", {"pair": pair})

    async def reflex_status(self):
        return await self._request("GET", "/reflex/status")

    async def reflex_logs(self):
        return await self._request("GET", "/reflex/logs")

    # ----------------------------- RISK LAYER -----------------------------

    async def risk_calculate(self, balance: float, sl_pips: float, pair: str):
        return await self._request("POST", "/risk/calculate", {"balance": balance, "sl_pips": sl_pips, "pair": pair})

    async def risk_summary(self):
        return await self._request("GET", "/risk/summary")

    async def risk_policy(self):
        return await self._request("GET", "/risk/policy")

    # ----------------------------- VAULT SYNC -----------------------------

    async def vault_sync(self):
        result = await self._request("POST", "/vault/sync")
        self.request_count += 1
        return result

    async def vault_status(self):
        return await self._request("GET", "/vault/status")

    # ----------------------------- REFLECTIVE & GPT -----------------------------

    async def reflective_trigger(self):
        return await self._request("POST", "/reflective/trigger")

    async def reflective_report(self):
        return await self._request("GET", "/reflective/report")

    async def gpt_bridge(self, message: str):
        payload = {"message": message}
        return await self._request("POST", "/gpt/bridge", payload)

    # ----------------------------- SYSTEM -----------------------------

    async def system_status(self):
        sys_status = await self._request("GET", "/system/status")
        if sys_status.get("status") == "ok" and self.request_count % 30 == 0:
            await self.vault_sync()  # Heartbeat auto sync
        return sys_status


# ----------------------------- TEST USAGE -----------------------------

async def main():
    tuyul = TuyulAgiBridgeV540()
    print(await tuyul.system_status())
    print(await tuyul.fusion_analyze("EURJPY", "H4"))
    print(await tuyul.risk_calculate(100000, 120, "XAUUSD"))
    await tuyul.close()

if __name__ == "__main__":
    asyncio.run(main())
