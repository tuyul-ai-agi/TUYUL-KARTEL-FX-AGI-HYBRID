"""
Run Hybrid Analysis
-------------------
Menjalankan analisa AGI Hybrid dari CLI.
"""

from pipeline.tuyul_hybrid_pipeline_v540 import TuyulHybridPipeline

if __name__ == "__main__":
    pipeline = TuyulHybridPipeline()
    result = pipeline.run(pair="XAUUSD")
    print("[HYBRID ANALYSIS RESULT]")
    print(result)
