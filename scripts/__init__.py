"""
🧠 TUYUL FX AGI v5.7.8 – Reflective CLI Map
--------------------------------------------
Pusat registrasi dan eksekusi semua script reflektif TUYUL FX.
Dijalankan oleh BOT–TJX atau user CLI untuk kontrol penuh Quad Repo Reflective System.

Bridge Protocol : RBP_v2.2
"""

import sys

from pipeline.quad_repo_sync_handler import run_quad_repo_sync
from scripts.generate_docs import generate_docs
from scripts.generate_openapi_docs import generate_openapi
from scripts.generate_swagger_ui import *  # noqa: F401,F403
from scripts.gpt_bridge_executor import run_bridge
from scripts.reflective_audit_reporter import generate_reflective_audit
from scripts.run_hybrid_analysis import run_analysis
from scripts.run_sync_vault import run_repo_sync
from scripts.sync_hybrid_repo import sync_hybrid_repo
from scripts.tuyul_cli_autopush import autopush
from scripts.vault_sync_reflective_fusion import sync_fusion_to_repo

__version__ = "5.7.8"
__bridge_protocol__ = "RBP_v2.2"
__integrity__ = 0.93
__bot__ = "TUYULBOT–TJX"

COMMANDS = {
    "docs": generate_docs,
    "openapi": generate_openapi,
    "swagger": lambda: print(
        "🌐 Jalankan Swagger UI dengan `python scripts/generate_swagger_ui.py`"
    ),
    "bridge": lambda: run_bridge("Analyze reflective bias continuation on EUR/USD"),
    "audit": generate_reflective_audit,
    "analyze": run_analysis,
    "sync": run_repo_sync,
    "hybrid": sync_hybrid_repo,
    "fusion": sync_fusion_to_repo,
    "push": autopush,
    "resync": run_quad_repo_sync,
}


def main() -> None:
    if len(sys.argv) < 2:
        print(
            """
🐺 TUYUL FX AGI Reflective CLI v5.7.8 (RBP_v2.2)
───────────────────────────────────────────────
Perintah tersedia:

  docs       → Generate reflective documentation
  openapi    → Generate OpenAPI YAML
  audit      → Generate reflective audit report
  analyze    → Run hybrid reflective pipeline
  sync       → Run Quad Repo sync (manual)
  resync     → Run adaptive repo re-sync
  fusion     → Sync Fusion Layer → Journal Repo
  hybrid     → Sync Hybrid Repo via GitHub
  bridge     → Run GPT Bridge reflective command
  push       → AutoPush Git commit (BOT–TJX)
  swagger    → Start Swagger UI (local port 9000)

Contoh:
  python -m scripts audit
  python -m scripts analyze
  python -m scripts resync
"""
        )
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd in COMMANDS:
        print(f"⚡ Executing TUYUL Reflective Command: {cmd.upper()} ...")
        COMMANDS[cmd]()
    else:
        print(f"❌ Command tidak dikenal: {cmd}")
        print("Gunakan `python -m scripts` untuk daftar perintah.")


if __name__ == "__main__":
    main()
