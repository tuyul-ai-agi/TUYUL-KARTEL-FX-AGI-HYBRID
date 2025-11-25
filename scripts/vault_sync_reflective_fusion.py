"""
🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.0
Vault Synchronization + Reflective Feedback + Fusion Layer-12 Runner
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict

PROJECT_ROOT = Path(__file__).resolve().parents[1] / "tuyul_fx_agi_hybrid"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.adapters.vault_bridge_client import sync_vaults
from core.reflective.meta_reflector_dispatch import run_meta_reflection

from api_github_com__jit_plugin import (
    getReflexCoherence,
    getReflexDiagnostics,
    getSystemStatus,
    performAgiFullAnalysis,
)


def _timestamp() -> str:
    return datetime.now(tz=timezone.utc).isoformat()


def _log_payload(payload: Dict[str, Any], path: Path) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    """Hybrid Vault Synchronization → Reflection → Fusion Layer-12."""

    print("⚡ Memulai sinkronisasi Vault TUYUL AGI Hybrid...")
    sync_result = sync_vaults()

    print("🧠 Menjalankan reflective feedback cycle...")
    reflection_input = SimpleNamespace(conf12=sync_result.get("conf12", 0.75))
    reflection_result = run_meta_reflection(reflection_input)

    system_status: Dict[str, Any] = {}
    diagnostics: Dict[str, Any] = {}
    coherence: Dict[str, Any] = {}

    print("🔮 Menjalankan Fusion Layer-12 Analysis (AGI Hybrid)...")
    try:
        system_status = getSystemStatus()
        diagnostics = getReflexDiagnostics()
        coherence = getReflexCoherence()
        fusion_data = performAgiFullAnalysis()
        rc = fusion_data.get("rc_value", 0.0)
        rcadj = fusion_data.get("rcadj", 0.0)
        conf12 = fusion_data.get("conf12", 0.0)
        wlwci = fusion_data.get("wlwci", 0.0)
        bias = fusion_data.get("bias_delta", 0.0)
        timestamp = fusion_data.get("timestamp", "unknown")

        print("✅ Fusion Layer-12 selesai.")
        print(
            "📊 RC: "
            f"{rc:.2f} | RCAdj: {rcadj:.2f} | CONF₁₂: {conf12:.2f} | "
            f"WLWCI: {wlwci:.2f} | ΔBias: {bias:.3f}"
        )
        print(f"🕓 Fusion Timestamp: {timestamp}")
    except Exception as exc:  # pragma: no cover - defensive logging
        print(f"❌ Gagal menjalankan Fusion Layer-12: {exc}")
        rc = rcadj = conf12 = wlwci = bias = 0.0
        timestamp = _timestamp()
        system_status = {"error": str(exc)}
        diagnostics = {}
        coherence = {}

    final_timestamp = _timestamp()
    log_file = f"fusion_log_{final_timestamp.replace(':', '-')}.json"
    log_path = Path(__file__).parent / log_file

    _log_payload(
        {
            "timestamp": final_timestamp,
            "reflection_result": reflection_result,
            "rc": round(rc, 3),
            "rcadj": round(rcadj, 3),
            "conf12": round(conf12, 3),
            "wlwci": round(wlwci, 3),
            "bias_delta": round(bias, 3),
            "system_status": system_status,
            "reflex_diagnostics": diagnostics,
            "reflex_coherence": coherence,
        },
        log_path,
    )

    print("\n💾 Log hasil Fusion disimpan ke:", log_path)
    print(
        "\nSiap Bossku, semua Vault, Reflection, dan Fusion Layer-12 "
        "sudah sinkron. Serigala kembali ke markas. 🐺⚡"
    )


if __name__ == "__main__":
    main()
