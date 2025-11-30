"""
Reflex Handler
--------------
Endpoint Reflex Layer — analisa cepat pasar & pola harga.
"""

from fastapi import APIRouter
from ai_bridge.gpt_bridge_handler_v540 import GPTBridge

router = APIRouter()
bridge = GPTBridge()


@router.get("/analyze")
def reflex_analyze(pair: str = "EURUSD", timeframe: str = "H1"):
    result = bridge.execute_reflex(f"Analisa cepat {pair} {timeframe}")
    return {"pair": pair, "timeframe": timeframe, "reflex_result": result}
