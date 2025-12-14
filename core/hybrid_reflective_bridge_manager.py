"""Hybrid Reflective Bridge Manager hook for neurotech ingestion."""

import subprocess
from typing import Any, Dict

from core.reflective.reflective_cycle import run_reflective_cycle as base_run_reflective_cycle


def run_reflective_cycle(pair: str = "XAUUSD", timeframe: str = "H4") -> Dict[str, Any]:
    """Run the reflective cycle and trigger the Neurotech RAG ingestor."""

    result = base_run_reflective_cycle(pair, timeframe)

    print("🔁 Menjalankan Neurotech RAG Ingestor...")
    subprocess.run(["python3", "rag_engine/knowledge_ingestion/optimized_neurotech_ingestor.py"])

    return result


if __name__ == "__main__":
    run_reflective_cycle()
