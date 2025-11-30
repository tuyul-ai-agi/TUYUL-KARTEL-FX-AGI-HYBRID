"""
generate_openapi_docs.py
========================

🔥 TUYUL AGI Hybrid v5.4.4-ULTRA
Script untuk auto-generate dokumentasi Swagger/OpenAPI statis (.html)
dari file `docs/openapi_tuyul_agi_hybrid_v5.4.4-ultra.yml`.

✅ Bisa dijalankan otomatis di Codespace, CI/CD workflow, atau manual di terminal:
   $ python scripts/generate_openapi_docs.py
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPENAPI_FILE = ROOT / "docs" / "openapi_tuyul_agi_hybrid_v5.4.4-ultra.yml"
OUTPUT_FILE = ROOT / "docs" / "openapi_docs.html"

def generate_docs():
    if not OPENAPI_FILE.exists():
        sys.exit(f"❌ File OpenAPI tidak ditemukan: {OPENAPI_FILE}")

    print("🚀 Menghasilkan dokumentasi Swagger statis...")
    cmd = [
        "npx",
        "redoc-cli",
        "bundle",
        str(OPENAPI_FILE),
        "-o",
        str(OUTPUT_FILE)
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Dokumentasi berhasil dibuat: {OUTPUT_FILE}")
    except subprocess.CalledProcessError as e:
        sys.exit(f"❌ Gagal membuat dokumentasi: {e}")

if __name__ == "__main__":
    generate_docs()
