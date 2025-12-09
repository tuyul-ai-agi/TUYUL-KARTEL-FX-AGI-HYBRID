#!/usr/bin/env bash
# ===========================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — postcreate.sh
# -----------------------------------------------------------
# Script otomatis dijalankan setelah Codespace selesai build.
# Fungsinya:
# - Generate Vault token unik
# - Inisialisasi submodule Vaults
# - Install dependencies Python AGI Hybrid
# - Jalankan reflective feed adapter check
# - Update log status ke Journal Vault
# ===========================================================

set -e
echo "🐺 [POSTCREATE] Inisialisasi TUYUL FX AGI HYBRID Environment..."
cd /workspaces/TUYUL-KARTEL-FX-AGI-HYBRID

# 1️⃣ Generate Vault Token
echo "🔑 Membuat VAULT_API_KEY..."
python3 - <<'PYCODE'
import secrets, json, os, time
vault_dir = "vaults"
os.makedirs(vault_dir, exist_ok=True)
token_data = {"VAULT_API_KEY": secrets.token_hex(16), "generated_at": time.time()}
with open(os.path.join(vault_dir, "vault_token.json"), "w") as f:
    json.dump(token_data, f, indent=2)
print(f"[TOKEN] VAULT_API_KEY: {token_data['VAULT_API_KEY']}")
PYCODE

# 2️⃣ Inisialisasi Submodules (Vault Repos)
echo "🧩 Menginisialisasi submodules..."
git submodule update --init --recursive || echo "⚠️ Submodule tidak ditemukan, lanjutkan."

# 3️⃣ Install Dependencies
echo "📦 Menginstal dependensi Python..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt || echo "⚠️ Tidak ada requirements.txt, lanjutkan."
pip install loguru fastapi aiofiles rich requests

# 4️⃣ Jalankan Feed Adapter Check (TwelveData)
echo "🌐 Menjalankan Reflective Adapter check..."
python3 - <<'PYCODE'
from adapters.twelvedata_adapter_v573r import fetch_and_store, reflective_journal_sync
import os
PAIR = os.getenv("TUYULFX_PAIR", "EUR/USD")
try:
    paths = fetch_and_store(PAIR)
    reflective_journal_sync(PAIR, paths)
    print(f"✅ Reflective data feed berhasil disinkronisasi untuk {PAIR}")
except Exception as e:
    print(f"⚠️ Tidak dapat mengambil feed TwelveData: {e}")
PYCODE

# 5️⃣ Update Journal Vault Log
echo "🧾 Mencatat log status ke Journal Vault..."
python3 - <<'PYCODE'
import json, os, time
journal_path = "vaults/journal_vault"
os.makedirs(journal_path, exist_ok=True)
status_log = {
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "status": "initialized",
    "bridge_protocol": "RBP v2.2",
    "environment": "codespace",
}
with open(os.path.join(journal_path, "postcreate_status.json"), "w") as f:
    json.dump(status_log, f, indent=2)
print("🧠 Reflective Journal Vault updated.")
PYCODE

# 6️⃣ Pesan Akhir
echo "------------------------------------------------------------"
echo "✅ TUYUL FX AGI HYBRID Codespace Siap!"
echo "Versi : v5.7.3r++ | Bridge: RBP v2.2 | Mode: Reflective"
echo "------------------------------------------------------------"
