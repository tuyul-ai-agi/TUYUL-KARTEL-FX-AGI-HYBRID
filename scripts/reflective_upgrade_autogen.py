#!/usr/bin/env python3
# =====================================================================
# TUYUL-FX AGI HYBRID REFLECTIVE AUTO-GENERATOR
# Version: v6.0 Quantum Hybrid Expansion
# File: scripts/reflective_upgrade_autogen.py
# =====================================================================
# 🧠 Purpose:
#   Membaca file reflective_upgrade_manifest_v6.0.yml dan secara otomatis
#   membuat struktur folder & file yang dibutuhkan untuk versi baru tanpa
#   menghapus atau menimpa file lama.
# =====================================================================

import os
import yaml
import json
from datetime import datetime

MANIFEST_PATH = "reflective_upgrade_manifest_v6.0.yml"
LOG_PATH = "logs/upgrade_autogen_log.json"
ROOT = os.getcwd()

# =====================================================================
# 🔧 Utility Functions
# =====================================================================

def load_manifest():
    """Membaca manifest upgrade YAML."""
    with open(MANIFEST_PATH, "r") as f:
        return yaml.safe_load(f)

def ensure_dir(path):
    """Pastikan direktori ada, jika belum maka buat."""
    os.makedirs(path, exist_ok=True)

def create_file(path, docstring):
    """Buat file dengan docstring reflektif standar."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(f'"""\n{docstring}\n"""\n\n')
            f.write("# TODO: Implement core reflective logic here.\n")
        return True
    return False

def log_event(logs, message, level="INFO"):
    """Tambahkan log event reflektif."""
    logs.append({
        "timestamp": datetime.utcnow().isoformat(),
        "level": level,
        "message": message
    })

def save_log(logs):
    """Simpan log operasi builder ke JSON."""
    ensure_dir(os.path.dirname(LOG_PATH))
    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)

# =====================================================================
# 🧩 Core Build Function
# =====================================================================

def build_from_manifest(manifest):
    logs = []
    log_event(logs, "Starting Reflective Upgrade Auto-Generation v6.0")

    upgrade_scope = manifest.get("upgrade_scope", [])
    for section in upgrade_scope:
        section_name = section.strip("/").split("/")[-1]
        if section_name not in manifest:
            log_event(logs, f"Skipping unknown section: {section_name}", "WARN")
            continue

        data = manifest[section_name]
        base_path = os.path.join(ROOT, data.get("base_path", section))
        ensure_dir(base_path)

        log_event(logs, f"📁 Created base folder: {base_path}")

        # Buat file utama
        for f_name in data.get("files", []):
            file_path = os.path.join(base_path, f_name)
            docstring = f"{section_name.upper()} MODULE - {data['description']}"
            if create_file(file_path, docstring):
                log_event(logs, f"🆕 File created: {file_path}")
            else:
                log_event(logs, f"⚠️ File already exists: {file_path}", "WARN")

        # Buat subfolder & file dalamnya
        for subfolder, subfiles in data.get("subfolders", {}).items():
            sub_path = os.path.join(base_path, subfolder)
            ensure_dir(sub_path)
            for subfile in subfiles:
                file_path = os.path.join(sub_path, subfile)
                docstring = f"{section_name.upper()} CONFIG/LOG - Auto-generated from manifest"
                if create_file(file_path, docstring):
                    log_event(logs, f"📄 Created: {file_path}")
                else:
                    log_event(logs, f"⚠️ Exists: {file_path}", "WARN")

    # Update version metadata
    version_meta = {
        "last_upgrade": datetime.utcnow().isoformat(),
        "version": manifest.get("version"),
        "codename": manifest.get("codename"),
        "safe_to_merge": manifest.get("meta", {}).get("safe_to_merge", True)
    }

    log_event(logs, f"✅ Upgrade complete: v{version_meta['version']} ({version_meta['codename']})")
    save_log(logs)

    # Simpan metadata upgrade ke configs/agi_reflective_evolution.yml
    evolution_path = os.path.join(ROOT, "configs", "agi_reflective_evolution.yml")
    with open(evolution_path, "a") as f:
        f.write(f"\n# Upgrade Applied on {version_meta['last_upgrade']}\n")
        yaml.safe_dump(version_meta, f)
    log_event(logs, f"🧠 Updated reflective evolution manifest: {evolution_path}")

# =====================================================================
# 🚀 Main Execution
# =====================================================================

if __name__ == "__main__":
    if not os.path.exists(MANIFEST_PATH):
        print(f"❌ Manifest file not found: {MANIFEST_PATH}")
        exit(1)

    manifest = load_manifest()
    build_from_manifest(manifest)
    print("✅ Reflective upgrade autogen complete. Logs saved to:", LOG_PATH)
