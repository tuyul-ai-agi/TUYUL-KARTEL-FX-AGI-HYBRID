"""
Hybrid Handler
--------------
Endpoint untuk menjalankan siklus penuh Reflex → Fusion → Reflective.
"""

from fastapi import APIRouter
from ai_bridge.gpt_bridge_handler_v540 import GPTBridge

router = APIRouter()
bridge = GPTBridge()


@router.post("/run_hybrid_cycle")
def run_hybrid_cycle(pair: str = "XAUUSD", timeframe: str = "H1"):
    reflex = bridge.execute_reflex(f"Analisa {pair} {timeframe}")
    fusion = bridge.execute_fusion(f"Gabungkan hasil Reflex {pair}")
    reflective = bridge.execute_reflective(f"Evaluasi hasil Fusion {pair}")
    return {
        "pair": pair,
        "timeframe": timeframe,
        "reflex_output": reflex,
        "fusion_output": fusion,
        "reflective_output": reflective
    }
