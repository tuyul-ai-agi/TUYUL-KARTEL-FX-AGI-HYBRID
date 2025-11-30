"""
Entrypoint utama TUYUL-KARTEL-FX-AGI-HYBRID
"""

from core.fushion.hybrid_fusion_orchestrator_v540 import HybridFusionOrchestrator
from core.reflective.reflective_cycle_core_v540 import ReflectiveCycle
from core.vaults.vault_integrity_checker import VaultIntegrityChecker

def main():
    print("🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.4.1 mulai...")
    orchestrator = HybridFusionOrchestrator()
    reflective = ReflectiveCycle()
    integrity = VaultIntegrityChecker()

    orchestrator.run()
    reflective.run_cycle()
    integrity.audit()

    print("✅ AGI Hybrid cycle complete.")

if __name__ == "__main__":
    main()
