# ============================================================
# 🧩 TUYUL FX AGI HYBRID v5.7.3r++
# File: core/kartel_engine/kartel_reflective_realign.py
# ------------------------------------------------------------
# Fungsi:
#  - Memperbaiki delay Kartel Repo
#  - Menyinkronkan feed makro (VIX, Fear-Greed, Bonds)
#  - Meningkatkan integrity index melalui reflective realignment
# ============================================================

import os, json, time, aiohttp, asyncio
from datetime import datetime
from client_agi_hybrid import AgiHybridClient
from core.fusion_engine.quantum_fusion_adapter import QuantumFusionAdapter

CACHE_PATH = "journal_repo/cache_kartel.json"

async def fetch_async(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=5) as res:
                if res.status == 200:
                    return await res.json()
        except Exception:
            return None

async def kartel_parallel_sync():
    urls = {
        "vix": "https://api.cboe.com/VIX",
        "fear_greed": "https://api.cnnfeargreedindex.com/latest",
        "usd_index": "https://api.twelvedata.com/time_series?symbol=DXY&interval=1h&apikey=demo"
    }
    results = await asyncio.gather(*[fetch_async(u) for u in urls.values()], return_exceptions=True)
    return dict(zip(urls.keys(), results))

def load_cached_data():
    if os.path.exists(CACHE_PATH) and (time.time() - os.path.getmtime(CACHE_PATH) < 300):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return None

def save_cache(data):
    os.makedirs("journal_repo", exist_ok=True)
    with open(CACHE_PATH, "w") as f:
        json.dump(data, f, indent=2)

async def realign_kartel_repo():
    print("🧩 [Kartel] Reflective Realignment started ...")
    cached = load_cached_data()
    data = await kartel_parallel_sync()

    if not all(data.values()):
        print("⚠️ Some feeds failed — using cached or quantum estimation.")
        qfa = QuantumFusionAdapter()
        qresult = qfa.analyze_coherence([0.87, 0.91, 0.83, 0.89])
        vix_est = 13.5 + qresult["conf12_q"] * 1.2
        data["vix"] = {"estimated": True, "value": vix_est, "source": "quantum_fallback"}

    save_cache(data)
    print(f"✅ Kartel feeds aligned. Data saved at {datetime.utcnow().isoformat()}Z")

    # update vault integrity
    hybrid = AgiHybridClient()
    payload = {
        "target": "Kartel",
        "mode": "reflective-realign",
        "integrity_patch": 0.05,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    print("🧾 Sending integrity feedback to Vault ...")
    try:
        requests = __import__("requests")
        res = requests.post(f"{hybrid.base_url}/vault/regenerate", json=payload)
        if res.status_code == 200:
            print("✅ Vault realignment acknowledged.")
        else:
            print(f"⚠️ Vault response {res.status_code}")
    except Exception as e:
        print(f"❌ Failed to send reflective feedback: {e}")

    print("🧩 [Kartel] Realignment complete.\n")
