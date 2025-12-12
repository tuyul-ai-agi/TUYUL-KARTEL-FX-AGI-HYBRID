# ============================================================
# 🧠 TUYUL FX AGI v5.8.2-HYBRID
# Reflex–Fusion Bridge Connector
# ============================================================

import json
import requests
from datetime import datetime
from twms_fusion_macro_mn import twms_fusion_macro_mn
import pandas as pd

# URL endpoint AGI Hybrid Core
HYBRID_API_URL = "https://api.hybridcore.tuyulkartel.ai/v1/fusion/analyze"
HYBRID_API_TOKEN = "YOUR_HYBRID_API_TOKEN"  # gunakan env var di deployment

def push_to_fusion_api(pair: str, timeframe: str, data: pd.DataFrame, fundamentals: dict):
    """
    Jalankan analisis TWMS Fusion Macro MN lalu kirim hasilnya
    ke AGI Reflex–Fusion endpoint /fusion/analyze
    """
    # Jalankan analisis TWMS
    result = twms_fusion_macro_mn(data, fundamentals)

    payload = {
        "pair": pair,
        "timeframe": timeframe,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "twms": result,
    }

    headers = {
        "Authorization": f"Bearer {HYBRID_API_TOKEN}",
        "Content-Type": "application/json",
    }

    print("🚀 Sending TWMS Fusion result to AGI Core ...")
    response = requests.post(HYBRID_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        print("✅ Fusion analysis updated successfully.")
    else:
        print(f"⚠️ Error {response.status_code}: {response.text}")

    return {
        "status": response.status_code,
        "fusion_response": response.text,
        "payload": payload,
    }


# ============================================================
# 🧪 DEMO (Offline Example)
# ============================================================
if __name__ == "__main__":
    import numpy as np

    np.random.seed(42)
    prices = np.cumsum(np.random.randn(120) * 0.5 + 0.1) + 100
    df = pd.DataFrame({"close": prices})

    fundamentals = {
        "bias": "bullish",
        "inflation_trend": 0.4,
        "rate_diff": 1.1,
    }

    result = push_to_fusion_api("USDCHF", "MN", df, fundamentals)
    print(json.dumps(result, indent=2))
