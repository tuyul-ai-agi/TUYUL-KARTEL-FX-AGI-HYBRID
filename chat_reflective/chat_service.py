"""
Reflective Chat Service v6.0
-----------------------------------------
FastAPI-powered conversational bridge for TUYUL-FX Quantum Hybrid System.
Connects Gemini or TUYUL Core to reflective adapters.
"""

from fastapi import FastAPI, Request
from chat_reflective.adapters.cognitive_adapter import CognitiveAdapter
from chat_reflective.adapters.reflective_adapter import ReflectiveAdapter
from chat_reflective.adapters.vault_adapter import VaultAdapter

app = FastAPI(title="TUYUL-FX Reflective Chat Service v6.0.0")

cognitive = CognitiveAdapter()
reflective = ReflectiveAdapter()
vault = VaultAdapter()

@app.post("/reflective/chat")
async def reflective_chat(req: Request):
    data = await req.json()
    user_input = data.get("message", "")
    user = data.get("user", "anonymous")

    encoded = cognitive.encode(user_input)
    reflection = reflective.process_reflection(encoded)
    vault.save_message(user, user_input)

    return {
        "input": encoded,
        "reflection": reflection,
        "recent_context": vault.read_recent()
    }

@app.get("/reflective/status")
async def reflective_status():
    return {"status": "active", "version": "6.0.0", "mode": "Quantum Hybrid Reflective"}
