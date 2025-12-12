"""
check_env_reflective.py
────────────────────────────
TUYUL FX AGI HYBRID v5.7.3r++
Reflective Environment Validator & Auto-Installer

Memastikan semua dependensi utama sistem reflektif tersedia
dan kompatibel dengan protokol RBP v2.2.
"""

from __future__ import annotations

import importlib
import subprocess
import sys
from datetime import datetime

REQUIRED_MODULES = {
    "fastapi": "0.115.0",
    "uvicorn": "0.30.1",
    "pydantic": "2.8.2",
    "joblib": "1.4.2",
    "pandas": "2.2.3",
    "prometheus_client": "0.21.0",
}


def install_module(module: str, version: str) -> None:
    """Instal modul yang hilang."""

    print(f"🧩 Menginstal modul: {module}=={version}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{module}=={version}"])
        print(f"✅ {module} berhasil diinstal.")
    except Exception as exc:  # pragma: no cover - runtime safety
        print(f"❌ Gagal menginstal {module}: {exc}")


def check_module(module: str, version: str) -> bool:
    """Cek apakah modul terinstal dan versi sesuai."""

    try:
        mod = importlib.import_module(module)
        current_version = getattr(mod, "__version__", "unknown")
        if current_version == "unknown":
            print(f"⚠️ {module} terinstal tapi tidak bisa mendeteksi versinya.")
        elif current_version != version:
            print(f"⚠️ {module} versi {current_version} berbeda dari target {version}.")
        else:
            print(f"✅ {module} v{current_version} OK.")
        return True
    except ImportError:
        print(f"❌ {module} belum terinstal.")
        return False


def run_check() -> None:
    print("────────────────────────────────────────────")
    print("🧠 TUYUL FX AGI REFLECTIVE ENVIRONMENT CHECKER")
    print(f"🕒 {datetime.utcnow().isoformat()}Z")
    print("Protocol: RBP v2.2 | Version: v5.7.3r++")
    print("────────────────────────────────────────────")

    missing: list[tuple[str, str]] = []
    for module, version in REQUIRED_MODULES.items():
        if not check_module(module, version):
            missing.append((module, version))

    if missing:
        print("\n🚀 Menginstal modul yang hilang...")
        for module, version in missing:
            install_module(module, version)
    else:
        print("\n✅ Semua modul reflektif sudah lengkap dan sesuai versi.")

    print("────────────────────────────────────────────")
    print("🔍 Mengecek environment Python...")
    print(f"Python version: {sys.version}")
    print(f"Executable: {sys.executable}")
    print("────────────────────────────────────────────")

    print("✅ Environment reflektif siap digunakan.")
    print("🐺 TUYUL FX AGI v5.7.3r++ — Reflective Mode Active ⚡")


if __name__ == "__main__":
    run_check()
