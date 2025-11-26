"""
🐺 TUYUL-KARTEL-FX-HYBRID v5.4.0
GPT Bridge Handler — Reflex–Cognition–Fusion Orchestrator

Menjalankan pipeline AGI Hybrid Layer-12:
Fusion → Vault Sync → Reflection → Journal Log
Auto-run ketika sistem Hybrid start.
"""

import os
import json
import time
from datetime import datetime
import requests

# ==============================
# 🔧 Konfigurasi Bridge
# ==============================
API_BASE = os.getenv("AGI_API_URL", "https://api.github.com")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "ghp_xxx_BOSS_TOKEN_xxx")
DEFAULT_PAIR = os.getenv("DEFAULT_PAIR", "XAUUSD")
DEFAULT_TF = os.getenv("DEFAULT_TF", "H1")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}


class GPTBridgeHandler:
    """
    Handler utama GPT–AGI Hybrid Bridge
    """

    def __init__(self):
        self.status = "initialized"
        self.last_sync = None
        self.api_url = API_BASE

    def _jit_call(self, method: str, endpoint: str, payload=None):
        """Helper untuk kirim request ke API Hybrid"""
        url = f"{self.api_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=HEADERS, json=payload)
            if response.status_code not in (200, 201, 204):
                raise Exception(f"HTTP {response.status_code}: {response.text}")
            if response.text.strip():
                return response.json()
            return {}
        except Exception as e:
            raise Exception(f"[BridgeError] {e}")

    def run_analysis(self, pair: str, timeframe: str):
        """
        Jalankan pipeline analisa penuh AGI Hybrid
        """
        print(f"🐺 Memulai AGI Hybrid Fusion untuk {pair} ({timeframe})...")

        # Step 1 — Trigger full fusion
        fusion = self._jit_call("POST", "/hybrid/runFullFusion")
        time.sleep(0.5)

        # Step 2 — Get Layer-12 result
        layer12 = self._jit_call("GET", "/hybrid/getFusionLayer12")
        time.sleep(0.5)

        # Step 3 — Push ke Journal
        journal = self._jit_call("POST", "/journal/pushReasoning")

        self.status = "completed"
        self.last_sync = datetime.utcnow().isoformat()

        return {
            "pair": pair,
            "timeframe": timeframe,
            "bridge_status": self.status,
            "last_sync": self.last_sync,
            "fusion_output": layer12,
            "journal_ack": journal
        }

# ====================================================
# 🚀 Auto-Run Section — Aktif saat sistem Hybrid start
# ====================================================

def run_gpt_hybrid_bridge(pair: str = DEFAULT_PAIR, timeframe: str = DEFAULT_TF):
    """
    Eksekusi langsung pipeline AGI Hybrid saat startup
    """
    print("==========================================")
    print("🐺 TUYUL KARTEL FX HYBRID v5.4.0 — AUTO BRIDGE START")
    print("==========================================")
    print(f"Pair Default: {pair} | Timeframe: {timeframe}\n")

    try:
        bridge = GPTBridgeHandler()
        print("🔗 Inisialisasi GPT Bridge...")
        result = bridge.run_analysis(pair, timeframe)

        print("\n--- ANALISA AGI HYBRID OTOMATIS ---")
        print(f"Pair: {result['pair']}")
        print(f"Timeframe: {result['timeframe']}")
        print(f"Bridge Status: {result['bridge_status']}")
        print(f"Last Sync: {result['last_sync']}")
        print(f"Fusion Output Keys: {list(result['fusion_output'].keys()) if isinstance(result['fusion_output'], dict) else 'Non-dict Output'}")
        print("------------------------------------------\n")
        print("🐺✅ AGI Fusion selesai dan disinkronisasi ke Vault.")
        print("📘 Hasil reasoning dicatat ke Journal Vault.\n")

        # Optional: simpan hasil ke log file
        os.makedirs("vaults/logs", exist_ok=True)
        with open("vaults/logs/bridge_autorun.log", "a") as logf:
            logf.write(f"[{result['last_sync']}] {pair} {timeframe} → {result['bridge_status']}\n")

    except Exception as e:
        print("❌ Error saat auto-run Bridge:")
        print(e)

    print("==========================================")
    print("Selesai — Reflexive Hybrid Mode [OK]")
    print("==========================================\n")


# Jalankan otomatis ketika sistem start
if __name__ == "__main__":
    run_gpt_hybrid_bridge()
