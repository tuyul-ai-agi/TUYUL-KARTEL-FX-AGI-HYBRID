"""
🌐 Reflective Live Bridge – TUYUL FX AGI HYBRID
-----------------------------------------
Koneksi ke API TUYUL untuk data real-time:
Fusion → Monte Carlo → VIX → Vault
-----------------------------------------
"""

import requests
from datetime import datetime

HYBRID_CORE_URL = "https://api.hybridcore.tuyulkartel.ai/v1"

def get_fusion_data(pair="XAUUSD", timeframe="H4"):
    """Ambil data fusion dari AGI Hybrid."""
    url = f"{HYBRID_CORE_URL}/fusion/analyze"
    try:
        res = requests.post(url, json={"pair": pair, "timeframe": timeframe}, timeout=20)
        data = res.json()
        data["timestamp"] = datetime.utcnow().isoformat()
        print(f"🧠 Fusion data OK: CONF₁₂={data.get('conf12')} WLWCI={data.get('wlwci')}")
        return data
    except Exception as e:
        print("⚠️ Gagal mengambil Fusion data:", e)
        return {}

def run_live_montecarlo(pair="XAUUSD"):
    """Menjalankan Monte Carlo 20k iter/90d secara live."""
    url = f"{HYBRID_CORE_URL}/fusion/montecarlo"
    try:
        res = requests.post(url, json={"pair": pair}, timeout=60)
        data = res.json()
        print(f"🎲 Monte Carlo OK: Win={data.get('win_probability')*100:.1f}%")
        return data
    except Exception as e:
        print("⚠️ Gagal menjalankan Monte Carlo:", e)
        return {}

def fetch_vix_status():
    """Ambil status VIX global (volatilitas & regime)."""
    url = f"{HYBRID_CORE_URL}/vix/status"
    try:
        res = requests.get(url, timeout=15)
        data = res.json()
        print(f"🌍 VIX={data.get('vix_level')} ({data.get('global_regime')})")
        return data
    except Exception as e:
        print("⚠️ Gagal mengambil data VIX:", e)
        return {}
