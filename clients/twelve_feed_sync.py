"""
🧠 TUYUL FX AGI v5.7.3r++ – TwelveData Feed Synchronizer
--------------------------------------------------------
File ini mengambil snapshot real-time seluruh pair utama (FX + Crypto)
langsung dari TwelveData API setiap 1 jam (3600 detik).
Hasilnya diformat seperti tabel real-time market dan disinkronkan ke Hybrid Vault.

Pipeline:
TwelveData → Reflex → Fusion → Reflective → Journal Vault
"""

import time
import requests
from datetime import datetime
from client_agi_hybrid import AgiHybridClient

API_KEY = "YOUR_TWELVEDATA_API_KEY"

PAIRS = [
    "EUR/USD", "USD/JPY", "GBP/USD", "USD/CHF", "USD/CAD",
    "AUD/USD", "NZD/USD", "BTC/USD", "ETH/USD", "XAU/USD"
]

def fetch_snapshot():
    """Ambil snapshot harga seluruh pair dari TwelveData"""
    snapshot = []
    for pair in PAIRS:
        url = "https://api.twelvedata.com/quote"
        params = {"symbol": pair, "apikey": API_KEY}
        r = requests.get(url, params=params)
        d = r.json()
        snapshot.append({
            "pair": pair,
            "bid": float(d.get("bid", 0)),
            "ask": float(d.get("ask", 0)),
            "high": float(d.get("high", 0)),
            "low": float(d.get("low", 0)),
            "change": float(d.get("change", 0)),
            "change_percent": d.get("percent_change", "0%"),
            "time": d.get("datetime", datetime.utcnow().strftime("%H:%M:%S"))
        })
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "loop_interval_minutes": 60,
        "pairs": snapshot
    }

def main_loop():
    """Loop otomatis setiap 1 jam untuk update feed dan sync Vault"""
    hybrid = AgiHybridClient()
    while True:
        data = fetch_snapshot()
        print(f"\n[🧩 SNAPSHOT] {data['timestamp']}")
        for p in data["pairs"]:
            print(f"{p['pair']}\t{p['bid']:.4f}\t{p['ask']:.4f}\t"
                  f"{p['high']:.4f}\t{p['low']:.4f}\t"
                  f"{p['change']:+.4f}\t{p['change_percent']}\t{p['time']}")
        hybrid.vault_sync()
        print("[✅] Vault synchronized successfully. Next update in 1 hour...\n")
        time.sleep(3600)  # tunggu 1 jam

if __name__ == "__main__":
    main_loop()
