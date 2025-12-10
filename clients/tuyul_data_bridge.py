"""
===========================================================
🐺 TUYUL FX AGI v5.7.3r++ – Data Bridge Module
-----------------------------------------------------------
Bridge ini berfungsi sebagai proxy lokal antara AGI Hybrid
dengan TwelveData API, agar sistem reflektif TUYUL dapat
mengambil data real-time tanpa langsung ke internet publik.

Komponen utama:
- Endpoint internal untuk /bridge/fetchLiveData & /bridge/updateFeeds
- Relay data real-time ke modul client_agi_hybrid.py
- Dapat berjalan sebagai service (Flask/FastAPI)
===========================================================
"""

from flask import Flask, request, jsonify
import requests
from datetime import datetime
import os

# Inisialisasi Flask App
app = Flask(__name__)

# Ambil API Key dari environment (atau repo secret)
API_KEY = os.getenv("TWELVEDATA_API_KEY", "YOUR_TWELVEDATA_API_KEY")

# Default Base URL TwelveData
BASE_URL = "https://api.twelvedata.com"

# Pair default untuk updateFeeds
DEFAULT_PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "XAU/USD",
    "BTC/USD", "ETH/USD", "AUD/USD", "NZD/USD"
]


@app.route("/bridge/fetchLiveData", methods=["GET"])
def fetch_live_data():
    """
    🔹 Ambil data live untuk 1 pair (real-time).
    Contoh:
        /bridge/fetchLiveData?pair=XAU/USD&interval=1h
    """
    pair = request.args.get("pair")
    interval = request.args.get("interval", "1min")

    if not pair:
        return jsonify({"error": "pair parameter required"}), 400

    try:
        url = f"{BASE_URL}/quote"
        params = {"symbol": pair, "apikey": API_KEY}
        response = requests.get(url, params=params)
        data = response.json()

        if "code" in data and data["code"] != 200:
            return jsonify({"error": data.get("message", "Invalid response")}), 400

        result = {
            "pair": pair,
            "price": data.get("price"),
            "bid": data.get("bid"),
            "ask": data.get("ask"),
            "high": data.get("high"),
            "low": data.get("low"),
            "change": data.get("change"),
            "change_percent": data.get("percent_change"),
            "timestamp": data.get("datetime", datetime.utcnow().isoformat() + "Z"),
            "source": "twelvedata"
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/bridge/updateFeeds", methods=["POST"])
def update_feeds():
    """
    🔹 Update semua pair utama dari TwelveData dan kirim hasil snapshot.
    Dipanggil otomatis oleh BOT reflektif tiap 1 jam.
    """
    results = []
    for pair in DEFAULT_PAIRS:
        url = f"{BASE_URL}/quote"
        params = {"symbol": pair, "apikey": API_KEY}
        r = requests.get(url, params=params)
        d = r.json()
        results.append({
            "pair": pair,
            "bid": d.get("bid"),
            "ask": d.get("ask"),
            "high": d.get("high"),
            "low": d.get("low"),
            "change": d.get("change"),
            "change_percent": d.get("percent_change"),
            "time": d.get("datetime", datetime.utcnow().strftime("%H:%M:%S"))
        })

    snapshot = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "loop_interval_minutes": 60,
        "pairs": results
    }

    return jsonify(snapshot)


@app.route("/bridge/status", methods=["GET"])
def bridge_status():
    """
    🔹 Endpoint kesehatan bridge.
    """
    return jsonify({
        "status": "Bridge Active",
        "version": "v5.7.3r++",
        "api_source": "TwelveData",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


if __name__ == "__main__":
    port = int(os.getenv("BRIDGE_PORT", 8000))
    print(f"[🧠 TUYUL DATA BRIDGE] Running on port {port} ...")
    app.run(host="0.0.0.0", port=port)
