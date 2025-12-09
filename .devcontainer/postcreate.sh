#!/usr/bin/env bash
# ===========================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — postcreate.sh (Reflective+)
# -----------------------------------------------------------
# Script otomatis setelah Codespace selesai build.
# Sekarang dilengkapi dengan:
#  - Logging ke logs/postcreate.log
#  - Audit ke Journal Vault
#  - Reflective initialization status
# ===========================================================

set -e

LOG_FILE="logs/postcreate.log"
mkdir -p logs vaults/journal_vault

echo "------------------------------------------------------------" | tee -a "$LOG_FILE"
echo "🐺 [POSTCREATE] Inisialisasi TUYUL FX AGI HYBRID Environment..." | tee -a "$LOG_FILE"
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" | tee -a "$LOG_FILE"
echo "------------------------------------------------------------" | tee -a "$LOG_FILE"
cd /workspaces/TUYUL-KARTEL-FX-AGI-HYBRID

# ===========================================================
# 1️⃣ Generate Vault Token
# ===========================================================
echo "🔑 Membuat VAULT_API_KEY..." | tee -a "$LOG_FILE"
python3 - <<'PYCODE'
import secrets, json, os, time
vault_dir = "vaults"
os.makedirs(vault_dir, exist_ok=True)
token_data = {"VAULT_API_KEY": secrets.token_hex(16), "generated_at": time.time()}
with open(os.path.join(vault_dir, "vault_token.json"), "w") as f:
    json.dump(token_data, f, indent=2)
print(f"[TOKEN] VAULT_API_KEY: {token_data['VAULT_API_KEY']}")
PYCODE >> "$LOG_FILE" 2>&1

# ===========================================================
# 2️⃣ Inisialisasi Submodules
# ===========================================================
echo "🧩 Menginisialisasi submodules..." | tee -a "$LOG_FILE"
git submodule update --init --recursive >> "$LOG_FILE" 2>&1 || echo "⚠️ Submodule tidak ditemukan." | tee -a "$LOG_FILE"

# ===========================================================
# 3️⃣ Install Dependencies
# ===========================================================
echo "📦 Menginstal dependensi Python..." | tee -a "$LOG_FILE"
pip install --upgrade pip setuptools wheel >> "$LOG_FILE" 2>&1
pip install -r requirements.txt >> "$LOG_FILE" 2>&1 || echo "⚠️ Tidak ada requirements.txt." | tee -a "$LOG_FILE"
pip install loguru fastapi aiofiles rich requests >> "$LOG_FILE" 2>&1

# ===========================================================
# 4️⃣ Jalankan Reflective Feed Adapter Check
# ===========================================================
echo "🌐 Menjalankan Reflective Adapter check (TwelveData)..." | tee -a "$LOG_FILE"
python3 - <<'PYCODE'
from adapters.twelvedata_adapter_v573r import fetch_and_store, reflective_journal_sync
import os
PAIR = os.getenv("TUYULFX_PAIR", "EUR/USD")
try:
    paths = fetch_and_store(PAIR)
    reflective_journal_sync(PAIR, paths)
    print(f"✅ Reflective data feed berhasil disinkronisasi untuk {PAIR}")
except Exception as e:
    print(f"⚠️ Gagal mengambil feed TwelveData: {e}")
PYCODE >> "$LOG_FILE" 2>&1

# ===========================================================
# 5️⃣ Update Journal Vault Log
# ===========================================================
echo "🧾 Mencatat log status ke Journal Vault..." | tee -a "$LOG_FILE"
python3 - <<'PYCODE'
import json, os, time
journal_path = "vaults/journal_vault"
os.makedirs(journal_path, exist_ok=True)
status_log = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "status": "initialized",
    "bridge_protocol": "RBP v2.2",
    "environment": "codespace",
    "log_file": "logs/postcreate.log"
}
with open(os.path.join(journal_path, "postcreate_status.json"), "w") as f:
    json.dump(status_log, f, indent=2)
print("🧠 Reflective Journal Vault updated.")
PYCODE >> "$LOG_FILE" 2>&1

# ===========================================================
# 6️⃣ Audit Reflektif
# ===========================================================
echo "🧠 Menulis audit sinkronisasi ke Journal Vault..." | tee -a "$LOG_FILE"
python3 - <<'PYCODE'
import json, os, time
audit_path = "vaults/journal_vault/postcreate_audit.json"
audit = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "summary": {
        "vault_token": os.path.exists("vaults/vault_token.json"),
        "feeds_dir": os.path.exists("knowledge/feeds"),
        "journal_log": os.path.exists("vaults/journal_vault/postcreate_status.json"),
        "reflective_bridge": "RBP v2.2"
    }
}
with open(audit_path, "w") as f:
    json.dump(audit, f, indent=2)
print(f"✅ Audit reflektif tersimpan di {audit_path}")
PYCODE >> "$LOG_FILE" 2>&1

# ===========================================================
# 7️⃣ Pesan Akhir
# ===========================================================
echo "------------------------------------------------------------" | tee -a "$LOG_FILE"
echo "✅ TUYUL FX AGI HYBRID Codespace Siap!" | tee -a "$LOG_FILE"
echo "Versi : v5.7.3r++ | Bridge: RBP v2.2 | Mode: Reflective+" | tee -a "$LOG_FILE"
echo "Log   : $LOG_FILE" | tee -a "$LOG_FILE"
echo "------------------------------------------------------------" | tee -a "$LOG_FILE"
