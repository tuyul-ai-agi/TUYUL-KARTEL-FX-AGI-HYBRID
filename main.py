"""
Entrypoint utama TUYUL-KARTEL-FX-AGI-HYBRID
"""

from core.fusion import FinalOutputReflectiveEngine, ReflectiveFusionOrchestrator
from core.repo.repo_health_monitor import RepoHealthMonitor


def main():
    print("🐺 TUYUL-KARTEL-FX-AGI-HYBRID v5.7.3r++ mulai...")
    orchestrator = ReflectiveFusionOrchestrator()
    final_output = FinalOutputReflectiveEngine()
    integrity = RepoHealthMonitor()

    sample_reflex = {"conf_reflex": 0.92, "rcadj": 0.08}
    sample_macro = {"conf_macro": 0.91, "rcadj": 0.07}
    fusion_state = orchestrator.run_fusion_cycle(sample_reflex, sample_macro)
    final_output.generate(fusion_state)
    integrity.audit()

    print("✅ AGI Hybrid cycle complete.")


if __name__ == "__main__":
    main()
