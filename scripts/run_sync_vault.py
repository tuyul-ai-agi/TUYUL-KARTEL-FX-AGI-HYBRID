"""
🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0
Vault Synchronization & Reflective Feedback Runner
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

PROJECT_ROOT = Path(__file__).resolve().parents[1] / "tuyul_fx_agi_hybrid"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.adapters.vault_bridge_client import sync_vaults
from core.reflective.meta_reflector_dispatch import run_meta_reflection


def main() -> None:
    """Run manual vault synchronization followed by a lightweight reflection."""

    print("⚡ Memulai sinkronisasi Vault TUYUL AGI Hybrid...")
    sync_result = sync_vaults()

    print("🧠 Menjalankan reflective feedback cycle...")
    reflection_input = SimpleNamespace(conf12=sync_result.get("conf12", 0.75))
    reflection_result = run_meta_reflection(reflection_input)

    timestamp = datetime.now(tz=timezone.utc).isoformat()
    print("\n✅ Sinkronisasi selesai.")
    print(f"🕓 Timestamp: {timestamp}")
    print(f"📘 Reflection Status: {reflection_result}")

    print("\nSiap Bossku, semua Vault udah sinkron. Serigala kembali ke markas. 🐺⚡")


if __name__ == "__main__":
    main()
