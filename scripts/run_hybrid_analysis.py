# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Run Hybrid Reflective Analysis
# ============================================================

from pipeline.tuyul_hybrid_pipeline_v578 import run_hybrid_pipeline


def run_analysis():
    print("🚀 Running Full Reflective Hybrid Analysis...")
    result = run_hybrid_pipeline("EUR/USD")
    print("✅ Analysis Completed:", result)
    return result


if __name__ == "__main__":
    run_analysis()
