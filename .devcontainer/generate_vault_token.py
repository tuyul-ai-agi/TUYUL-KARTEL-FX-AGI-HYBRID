#!/usr/bin/env python3
"""
generate_vault_token.py
=======================

Script otomatis untuk membuat dan menginject VAULT_API_KEY ke environment Codespace.

🔹 Gunakan GH_TOKEN (yang sudah diset di Secrets Codespaces)
🔹 Generate token GitHub via API (dengan permission repo, workflow, read:org)
🔹 Simpan hasil ke environment runtime Codespace

By: 🐺 TUYUL HYBRID AGI v5.4.1
"""

import os
import json
import requests
from pathlib import Path

# ====================================================
# Konfigurasi awal
# ====================================================
GITHUB_API = "https://api.github.com"
OWNER = "tjx578"
TOKEN_ALIAS = "TUYUL_VAULT_TOKEN"
ENV_FILE = Path(".devcontainer/.env.generated")

# Ambil GH_TOKEN dari environment
GH_TOKEN = os.getenv("GH_TOKEN")

if not GH_TOKEN:
    raise RuntimeError("❌ GH_TOKEN tidak ditemukan. Pastikan sudah diset di Codespace Secrets.")

headers = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

# ====================================================
# 1️⃣ Generate token baru via API
# ====================================================
print("🔑 Membuat Personal Access Token untuk Vault...")

create_token_url = f"{GITHUB_API}/authorizations"

payload = {
    "note": TOKEN_ALIAS,
    "scopes": ["repo", "workflow", "read:org", "read:packages"],
}

response = requests.post(create_token_url, headers=headers, json=payload)

if response.status_code not in (200, 201):
    print(f"❌ Gagal membuat token Vault. Status: {response.status_code}")
    print("Respon:", response.text)
    exit(1)

vault_token = response.json().get("token")

if not vault_token:
    raise ValueError("❌ Gagal membaca token dari response API GitHub.")

print("✅ Token Vault berhasil dibuat.")
print("🔒 Token disimpan lokal dan diinject ke environment.")

# ====================================================
# 2️⃣ Simpan ke file .env runtime Codespace
# ====================================================
ENV_FILE.parent.mkdir(parents=True, exist_ok=True)
ENV_FILE.write_text(f"VAULT_API_KEY={vault_token}\n")

# Inject ke session environment aktif
os.environ["VAULT_API_KEY"] = vault_token

# ====================================================
# 3️⃣ Update file configs Vault (auto-sync)
# ====================================================
CONFIG_DIR = Path("configs")
for yaml_file in CONFIG_DIR.glob("*_vault.yaml"):
    text = yaml_file.read_text()
    if "auth_token" not in text:
        updated = text.strip() + f"\n  auth_token: {vault_token}\n"
        yaml_file.write_text(updated)
        print(f"🔧 Token ditambahkan ke {yaml_file.name}")
    else:
        print(f"🟡 {yaml_file.name} sudah memiliki token field, dilewati.")

# ====================================================
# 4️⃣ Konfirmasi akhir
# ====================================================
print("\n✅ Semua konfigurasi Vault siap.")
print("🔹 VAULT_API_KEY aktif di environment.")
print("🔹 Konfigurasi diperbarui di configs/*.yaml.")
print("🐺 TUYUL Vault Sync Engine siap digunakan.\n")
