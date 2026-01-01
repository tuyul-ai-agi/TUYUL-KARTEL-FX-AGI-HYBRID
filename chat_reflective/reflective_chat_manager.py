"""Reflective Chat Manager v6.0
-----------------------------------------
Core orchestrator connecting GeminiBridge, Prompt Templates,
and Reflective Awareness State for TUYUL-FX Quantum Hybrid System.
"""
import os
from datetime import datetime

from chat_reflective.gemini_bridge import GeminiBridge
from chat_reflective.adapters.vault_adapter import VaultAdapter


class ReflectiveChatManager:
    def __init__(self):
        self.bridge = GeminiBridge()
        self.vault = VaultAdapter()
        self.template_path = "chat_reflective/prompt_templates/"
        self.state = {"coherence": 0.93, "last_update": None}

    def _load_template(self, filename: str) -> str:
        path = os.path.join(self.template_path, filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def compose_prompt(self, user_input: str) -> str:
        meta = self._load_template("meta_prompt.txt")
        reasoning = self._load_template("reasoning_prompt.txt")
        reflective = self._load_template("reflective_prompt.txt")
        combined = f"{meta}\n\n{reasoning}\n\n{reflective}\n\nUser: {user_input}\nSystem:"
        return combined

    def chat(self, user_input: str, user: str = "anonymous") -> dict:
        """Run full reflective chat cycle."""
        prompt = self.compose_prompt(user_input)
        response = self.bridge.query(prompt)
        self.vault.save_message(user, user_input)

        self.state["last_update"] = datetime.utcnow().isoformat()
        self.state["coherence"] = round(self.state["coherence"] * 0.98 + 0.02, 3)

        return {
            "input": user_input,
            "reflective_response": response,
            "coherence": self.state["coherence"],
            "timestamp": self.state["last_update"],
        }


if __name__ == "__main__":  # pragma: no cover - manual CLI
    mgr = ReflectiveChatManager()
    print("🧠 Reflective Chat Manager v6.0 Initialized")
    while True:
        text = input("💬 You: ")
        out = mgr.chat(text)
        print(f"🤖 TUYUL: {out['reflective_response']}\n🪞 Coherence: {out['coherence']}")

"""
User Input
   ↓
Cognitive Adapter → Tokenisasi konteks
   ↓
ReflectiveChatManager → Gabungkan Prompt (Meta + Reasoning + Reflective)
   ↓
GeminiBridge → Query ke Gemini (Generative)
   ↓
VaultAdapter → Simpan ke Journal Repo
   ↓
Reflective Log + Coherence Update
"""
