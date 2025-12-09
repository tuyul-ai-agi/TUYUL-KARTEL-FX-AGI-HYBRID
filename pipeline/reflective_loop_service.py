#!/usr/bin/env python3
# ==============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — Reflective Loop Service (Adaptive)
# --------------------------------------------------------------
# Service reflektif adaptif yang berjalan 24/7.
# - Menjalankan ReflectiveMetaCycle() secara berkala
# - Interval adaptif berdasarkan Regime State (Tranquil/Stressed/Crisis)
# - Mencatat hasilnya ke Journal Vault dan logs
# - Sinkron dengan BOT tuyulagibot-tjx (Bridge RBP v2.2)
# ==============================================================

import os
import time
import json
from datetime import datetime
from loguru import logger
from pathlib import Path

from pipeline.reflective_meta_cycle import ReflectiveMetaCycle

# ==============================================================
# Konfigurasi
# ==============================================================

LOG_PATH = Path("logs/reflective_loop_service.log")
JOURNAL_PATH = Path("vaults/journal_vault/reflective_loop_log.json")

DEFAULT_INTERVALS = {
    "Tranquil": 3600,   # 1 jam
    "Stressed": 1800,   # 30 menit
    "Crisis": 900       # 15 menit
}

logger.add(LOG_PATH, rotation="5 MB", retention="14 days", encoding="utf-8")
logger.info("🐺 Reflective Loop Service v5.7.3r++ [Adaptive Mode] initialized.")


# ==============================================================
# Utility Functions
# ==============================================================

def write_journal_log(entry: dict):
    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    journal_data = []
    if JOURNAL_PATH.exists():
        try:
            journal_data = json.load(open(JOURNAL_PATH, "r", encoding="utf-8"))
        except Exception:
            journal_data = []
    journal_data.append(entry)
    with open(JOURNAL_PATH, "w", encoding="utf-8") as f:
        json.dump(journal_data[-48:], f, indent=2)  # Simpan max 48 entri (2 hari)
    logger.info(f"🧾 Journal updated → {JOURNAL_PATH}")


def notify_bot(result: dict):
    """Simulasi notifikasi ke BOT tuyulagibot-tjx."""
    if os.getenv("ENABLE_BOT_NOTIFY", "true").lower() != "true":
        return
    regime = result.get("based_on", "Unknown")
    logger.info(f"🤖 BOT tuyulagibot-tjx notified: regime={regime}")


def get_adaptive_interval(regime_state: str) -> int:
    """Menentukan interval loop berdasarkan kondisi pasar."""
    regime = regime_state.capitalize()
    return DEFAULT_INTERVALS.get(regime, 3600)


# ==============================================================
# Main Reflective Loop
# ==============================================================

def reflective_loop():
    cycle = ReflectiveMetaCycle()
    regime_state = "Tranquil"

    while True:
        try:
            logger.info(f"🔁 Executing ReflectiveMetaCycle() [Current Regime: {regime_state}] ...")
            result = cycle.execute()

            regime_state = result.get("based_on", "Tranquil")
            next_interval = get_adaptive_interval(regime_state)

            entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "status": result.get("status", "ok"),
                "based_on": regime_state,
                "bridge_protocol": result.get("bridge_protocol", "RBP v2.2"),
                "version": result.get("version", "v5.7.3r++"),
                "next_interval": next_interval
            }

            write_journal_log(entry)
            notify_bot(result)

            logger.success(f"✅ Reflective cycle completed — next cycle in {next_interval/60:.0f} min.")
        except Exception as e:
            logger.exception(f"💥 Error during reflective cycle: {e}")
            next_interval = 3600  # fallback 1 jam

        time.sleep(next_interval)


# ==============================================================
# Entry Point
# ==============================================================

if __name__ == "__main__":
    try:
        reflective_loop()
    except KeyboardInterrupt:
        logger.warning("🧠 Reflective Loop stopped manually.")
