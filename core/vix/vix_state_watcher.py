#!/usr/bin/env python3
# ==============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — VIX State Watcher
# --------------------------------------------------------------
# Modul untuk memantau volatilitas global (CBOE VIX) secara real-time.
# - Mengambil data dari TwelveData API
# - Menentukan regime state (Tranquil / Stressed / Crisis)
# - Menulis hasil ke Journal Vault untuk digunakan Reflective Loop
# ==============================================================

import os
import json
import time
import requests
from datetime import datetime
from loguru import logger
from pathlib import Path

# ==============================================================
# Konfigurasi dasar
# ==============================================================

API_KEY = os.getenv("TWELVEDATA_API_KEY")
SYMBOL = "VIX"
INTERVAL = "1h"
JOURNAL_PATH = Path("vaults/journal_vault/vix_state.json")
LOG_PATH = Path("logs/vix_state_watcher.log")

THRESHOLDS = {
    "Tranquil": 15,
    "Stressed": 25,
    "Crisis": 40
}

REFRESH_INTERVAL = int(os.getenv("VIX_REFRESH_INTERVAL", 1800))  # Default: 30 menit

logger.add(LOG_PATH, rotation="3 MB", retention="7 days", encoding="utf-8")
logger.info("🌐 VIX State Watcher v5.7.3r++ initialized.")


# ==============================================================
# Fungsi utama
# ==============================================================

def fetch_vix_value() -> float:
    """Mengambil nilai terakhir dari CBOE VIX melalui TwelveData."""
    if not API_KEY:
        raise ValueError("TWELVEDATA_API_KEY belum diset di environment variable.")

    url = (
        f"https://api.twelvedata.com/quote?symbol={SYMBOL}&apikey={API_KEY}"
    )
    response = requests.get(url, timeout=15)
    if response.status_code != 200:
        raise ConnectionError(f"API error: {response.status_code} {response.text}")
    data = response.json()
    if "close" not in data:
        raise ValueError(f"Invalid response: {data}")
    return float(data["close"])


def determine_regime(vix_value: float) -> str:
    """Menentukan regime state berdasarkan nilai VIX."""
    if vix_value < THRESHOLDS["Tranquil"]:
        return "Tranquil"
    elif vix_value < THRESHOLDS["Stressed"]:
        return "Stressed"
    return "Crisis"


def write_journal(vix_value: float, regime: str):
    """Menulis hasil VIX state ke Journal Vault."""
    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "vix_value": vix_value,
        "regime_state": regime,
        "bridge_protocol": "RBP v2.2",
        "version": "v5.7.3r++"
    }
    with open(JOURNAL_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    logger.info(f"🧾 VIX state updated → {JOURNAL_PATH}")
    return state


def vix_state_watcher():
    """Loop utama pemantau VIX Index."""
    while True:
        try:
            vix_value = fetch_vix_value()
            regime = determine_regime(vix_value)
            result = write_journal(vix_value, regime)
            logger.success(f"✅ VIX={vix_value:.2f} → Regime={regime}")
        except Exception as e:
            logger.exception(f"💥 Gagal memperbarui VIX state: {e}")
        time.sleep(REFRESH_INTERVAL)


# ==============================================================
# Entry point
# ==============================================================

if __name__ == "__main__":
    try:
        vix_state_watcher()
    except KeyboardInterrupt:
        logger.warning("🧠 VIX Watcher dihentikan manual.")
