
"""
🐺 TUYUL FX ULTRA WOLF v5.4.1 — HYBRID AGI BRIDGE MODULE
=========================================================
Bridge utama antara TUYUL FX runtime (Fusion, Reflex, Risk)
dan subsistem eksternal (Vault, Reflective Engine, GPT Interface).

✅ Pembaruan v5.4.1:
- Integrasi AutoSync (Differential Mode, SHA256-based)
- Hook otomatis ke vault_autosync_v541.py setelah build selesai
- Reflective learning trigger otomatis setelah Fusion
- Auto heartbeat vault sync setiap 30 request
- Async architecture (aiohttp-based)
"""

import aiohttp
import asyncio
import json
import time
from datetime import datetime
from tuyul_fx_agi_hybrid.core.bridge.vault_autosync_v541 import scan_and_sync

class TuyulAgiBridgeV540:
    def __init__(self, base_url="https://api.tuyulfx.ai/v5.4.0", api_key=None, autosync=True):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = None
        self.request_count = 0
        self.autosync = autosync

    # ==========================================================
    # 🧠 SESSION MANAGEMENT
    # ==========================================================
    async def _ensure_session(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    # ==========================================================
    # ⚙️ GENERIC REQUEST HANDLER
    # ==========================================================
    async def _request(self, method, path, payload=None, retries=3):
        await self._ensure_session()
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"  # Optional API key support

        for attempt in range(1, retries + 1):
            start_time = time.time()
            try:
                async with self.session.request(method, url, headers=headers, json=payload, timeout=25) as resp:
                    latency = round((time.time() - start_time) * 1000, 2)
                    data = await resp.json(content_type=None)
                    self.request_count += 1
                    result = {
                        "status": "ok",
                        "endpoint": path,
                        "data": data,
                        "latency_ms": latency,
                        "timestamp": datetime.utcnow().isoformat(),
                    }

                    # Heartbeat: Sync every 30 requests
                    if self.request_count % 30 == 0 and self.autosync:
                        print("💾 Heartbeat AutoSync Triggered (every 30 requests)")
                        scan_and_sync("/mnt/data")

                    return result
            except Exception as e:
                if attempt == retries:
                    return {"error": True, "message": str(e), "endpoint": path, "retries": retries}
                await asyncio.sleep(1.5 * attempt)

    # ==========================================================
    # 🔹 FUSION LAYER
    # ==========================================================
    async def fusion_analyze(self, pair: str, timeframe: str):
        """
        Jalankan analisis penuh Fusion Layer (CONF₁₂, WLWCI, Reflex coupling)
        """
        result = await self._request("POST", "/fusion/analyze", {"pair": pair, "timeframe": timeframe})
        if result.get("status") == "ok":
            print("🧠 Fusion layer complete. Triggering reflective learning ...")
            await self.reflective_trigger()
            if self.autosync:
                print("📡 AutoSync setelah Fusion ...")
                scan_and_sync("/mnt/data")
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

    # ==========================================================
    # ⚡ REFLEX LAYER
    # ==========================================================
    async def reflex_analyze(self, pair: str):
        return await self._request("POST", "/reflex/analyze", {"pair": pair})

    async def reflex_status(self):
        return await self._request("GET", "/reflex/status")

    async def reflex_logs(self):
        return await self._request("GET", "/reflex/logs")

    # ==========================================================
    # 💥 RISK LAYER
    # ==========================================================
    async def risk_calculate(self, balance: float, sl_pips: float, pair: str):
        return await self._request("POST", "/risk/calculate", {"balance": balance, "sl_pips": sl_pips, "pair": pair})

    async def risk_summary(self):
        return await self._request("GET", "/risk/summary")

    async def risk_policy(self):
        return await self._request("GET", "/risk/policy")

    # ==========================================================
    # 📦 VAULT SYNC + STATUS
    # ==========================================================
    async def vault_sync(self):
        """
        Jalankan sinkronisasi vault manual (Hybrid + Knowledge + Journal)
        """
        print("📡 Menjalankan sinkronisasi vault manual ...")
        result = await self._request("POST", "/vault/sync")
        if result.get("status") == "ok" and self.autosync:
            scan_and_sync("/mnt/data")
        return result

    async def vault_status(self):
        return await self._request("GET", "/vault/status")

    # ==========================================================
    # 🧬 REFLECTIVE & GPT INTERFACE
    # ==========================================================
    async def reflective_trigger(self):
        """
        Aktifkan proses pembelajaran reflektif (post-Fusion reinforcement)
        """
        print("🔁 Reflective cycle triggered ...")
        return await self._request("POST", "/reflective/trigger")

    async def reflective_report(self):
        return await self._request("GET", "/reflective/report")

    async def gpt_bridge(self, message: str):
        payload = {"message": message}
        return await self._request("POST", "/gpt/bridge", payload)

    # ==========================================================
    # 🖥️ SYSTEM STATUS + AUTO HEARTBEAT
    # ==========================================================
    async def system_status(self):
        """
        Mengecek status sistem utama TUYUL FX (uptime, versi, latensi)
        """
        sys_status = await self._request("GET", "/system/status")
        if sys_status.get("status") == "ok" and self.request_count % 30 == 0 and self.autosync:
            print("💾 Heartbeat sync triggered (via system_status)")
            scan_and_sync("/mnt/data")
        return sys_status


# ==========================================================
# 🧩 BUILD HOOK — AutoSync setelah build
# ==========================================================
async def run_build_pipeline():
    """
    Simulasi pipeline build penuh TUYUL FX.
    Setelah selesai, AutoSync akan dijalankan otomatis.
    """
    print(f"\n⚙️  TUYUL HYBRID BUILD STARTED — {datetime.utcnow().isoformat()}")
    await asyncio.sleep(1.2)
    print("✅ Build pipeline selesai.")
    print("🧠 Menjalankan AutoSync vault setelah build ...")
    scan_and_sync("/mnt/data")
    print("📦 Sinkronisasi vault selesai.")
    print("🐺 TUYUL FX siap ke fase reflektif berikutnya.\n")

# ==========================================================
# 🚀 TEST USAGE
# ==========================================================
async def main():
    tuyul = TuyulAgiBridgeV540(api_key=None, autosync=True)
    print(await tuyul.system_status())
    print(await tuyul.fusion_analyze("EURJPY", "H4"))
    print(await tuyul.risk_calculate(100000, 120, "XAUUSD"))
    await tuyul.close()

if __name__ == "__main__":
    asyncio.run(main())
