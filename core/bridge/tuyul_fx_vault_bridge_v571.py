#!/usr/bin/env python3
"""
🧠 TUYUL FX VAULT BRIDGE v5.7.1-HYBRID+
Quad-Vault Reflective Synchronization Orchestrator.
"""

from __future__ import annotations

import asyncio
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from tuyul_agi_hybrid.fusion.vault_sync import vault_sync
from tuyul_agi_hybrid.reflective_cycle import run_reflective_cycle
from tuyul_fx_knowledge_agi.fibonacci_confluence_engine import FibConfluenceEngine
from tuyul_fx_knowledge_agi.smartmoney import SmartMoneyAnalyzer
from tuyul_journal_vault_agi.reflective_log import ReflectiveJournal
from tuyul_kartel_knowledge_agi.vix_rsd_hybrid import VIXHybridMonitor

LOG_PATH = Path("data/vault/bridge_quad_log.jsonl")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

CONFIG = {
    "interval_sec": 180,
    "version": "v5.7.1-Hybrid+",
}


class TuyulFXVaultBridgeQuad:
    """Bridge utama yang mengorkestrasi sinkronisasi lintas empat Vault."""

    def __init__(self, pair: str = "GBPUSD") -> None:
        self.pair = pair
        self.smartmoney = SmartMoneyAnalyzer(pair)
        self.fibo = FibConfluenceEngine(pair)
        self.vix = VIXHybridMonitor()
        self.journal = ReflectiveJournal()
        self.active = False

    async def run_cycle(self) -> Dict[str, Any]:
        t0 = time.time()
        timestamp = datetime.utcnow().isoformat()
        print(f"\n🧠 [Quad-Vault Sync] Cycle started at {timestamp} | Pair={self.pair}")

        sm_bias = self.smartmoney.compute_bias()
        fib_data = self.fibo.evaluate_confluence()
        vix_regime = self.vix.evaluate_global_regime()

        vault_state = vault_sync()
        reflection = run_reflective_cycle()

        report = {
            "timestamp": timestamp,
            "pair": self.pair,
            "smartmoney": sm_bias,
            "fibonacci": fib_data,
            "vix_regime": vix_regime,
            "vault_state": vault_state,
            "reflective": reflection,
            "meta": {
                "version": CONFIG["version"],
                "latency_ms": round((time.time() - t0) * 1000, 2),
            },
        }

        self.journal.log_cycle(
            self.pair, sm_flow=sm_bias, vix_context=vix_regime, vault_state=vault_state
        )

        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(report) + "\n")

        print(
            "✅ [Quad-Vault Sync] Done in"
            f" {report['meta']['latency_ms']} ms | CONF₁₂={vault_state.get('conf12', 'N/A')}"
        )
        return report

    async def run_loop(self) -> None:
        self.active = True
        print(f"🚀 TUYUL FX Vault Bridge Quad v{CONFIG['version']} starting...")
        while self.active:
            try:
                await self.run_cycle()
                await asyncio.sleep(CONFIG["interval_sec"])
            except Exception as exc:  # noqa: BLE001
                err = {"timestamp": datetime.utcnow().isoformat(), "error": str(exc)}
                print(f"⚠️ [Bridge Error] {exc}")
                self.journal.write_error(err)
                await asyncio.sleep(15)

    def stop(self) -> None:
        self.active = False
        print("🛑 TUYUL Quad-Vault Bridge stopped.")


if __name__ == "__main__":
    bridge = TuyulFXVaultBridgeQuad(pair="EURUSD")
    try:
        asyncio.run(bridge.run_loop())
    except KeyboardInterrupt:
        bridge.stop()
