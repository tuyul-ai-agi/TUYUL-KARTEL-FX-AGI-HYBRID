#!/usr/bin/env python3
# ==============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — Reflective Loop Service
# --------------------------------------------------------------
# Service reflektif yang berjalan 24/7 di container `reflective-loop`.
# - Menjalankan ReflectiveMetaCycle setiap 1 jam
# - Mencatat hasilnya ke Journal Vault dan logs
# - Sinkron dengan BOT (via tuyulagibot-tjx bridge)
# ==============================================================

import os
import time
import json
from datetime import datetime
from loguru import logger
from pathlib import Path
from pipeline.reflective_meta_cycle import ReflectiveMetaCycle

# ==============================================================
# Konfigurasi dasar
# ==============================================================

LOG_PATH = Path("logs/reflective_loop_service.log")
JOURNAL_PATH = Path("vaults/journal_vault/reflective_loop_log.json")
INTERVAL = int(os.getenv("REFLECTIVE_LOOP_INTERVAL", 3600))  # Default: 1 jam (3600 detik)

logger.add(LOG_PATH, rotation="5 MB", retention="14 days", encoding="utf-8")
logger.info("🐺 Reflective Loop Service v5.7.3r++ started (interval = 1 hour)")

# ==============================================================
# Fungsi utilitas
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
        json.dump(journal_data[-24:], f, indent=2)  # Simpan max 24 log (1 hari)
    logger.info(f"🧾 Reflective log updated → {JOURNAL_PATH}")


def notify_bot(result: dict):
    """Simulasi notifikasi ke BOT tuyulagibot-tjx."""
    bridge_status = os.getenv("ENABLE_BOT_NOTIFY", "true").lower() == "true"
    if not bridge_status:
        return
    logger.info(f"🤖 BOT tuyulagibot-tjx notified: regime={result.get('based_on')}")


# ==============================================================
# Main Reflective Loop
# ==============================================================

def reflective_loop():
    cycle = ReflectiveMetaCycle()

    while True:
        try:
            logger.info("🔁 Executing ReflectiveMetaCycle() ...")
            result = cycle.execute()

            entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "status": result.get("status", "ok"),
                "based_on": result.get("based_on"),
                "bridge_protocol": result.get("bridge_protocol", "RBP v2.2"),
                "version": result.get("version", "v5.7.3r++"),
            }

            write_journal_log(entry)
            notify_bot(result)
            logger.success(f"✅ Reflective cycle completed at {entry['timestamp']}")

        except Exception as e:
            logger.exception(f"💥 Error during reflective cycle: {e}")

        logger.info(f"🕒 Sleeping for {INTERVAL/3600:.1f} hour(s)...")
        time.sleep(INTERVAL)


# ==============================================================
# Entry Point
# ==============================================================

if __name__ == "__main__":
    try:
        reflective_loop()
    except KeyboardInterrupt:
        logger.warning("🧠 Reflective Loop stopped manually.")
