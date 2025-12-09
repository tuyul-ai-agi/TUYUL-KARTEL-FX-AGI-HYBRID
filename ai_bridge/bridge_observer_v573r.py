"""
Bridge Observer v5.7.3r++
-------------------------
Observer reflektif untuk memantau status sinkronisasi antar repo
dan memicu re-learning bila coherence turun di bawah threshold.
"""

import asyncio
import json
from datetime import datetime
from aiohttp import ClientSession

REFLECTIVE_ENDPOINT = "http://localhost:8501/status"
COHERENCE_THRESHOLD = 0.82

async def check_bridge_status():
    async with ClientSession() as session:
        try:
            async with session.get(REFLECTIVE_ENDPOINT) as res:
                data = await res.json()
                coherence = data.get("coherence", 0)
                if coherence < COHERENCE_THRESHOLD:
                    print(f"[WARN] Coherence drop detected ({coherence}) → triggering re-sync.")
                    await trigger_reflective_sync()
                else:
                    print(f"[OK] Coherence stable: {coherence}")
        except Exception as e:
            print(f"[ERROR] Observer failed: {e}")

async def trigger_reflective_sync():
    timestamp = datetime.utcnow().isoformat()
    log = {"timestamp": timestamp, "action": "reflective_sync_triggered"}
    with open("logs/bridge_observer.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")
    print("[SYNC] Reflective Sync Triggered via Observer.")

if __name__ == "__main__":
    asyncio.run(check_bridge_status())
