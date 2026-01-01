"""
Reflex Console v6.0
-----------------------------------------
Command-line reflective console for TUYUL Cognitive System.
Allows real-time reasoning and coherence inspection.
"""

from chat_reflective.reflective_chat_manager import ReflectiveChatManager

from cognitive_frontend.context_interpreter import ContextInterpreter


class ReflexConsole:
    def __init__(self):
        self.chat = ReflectiveChatManager()
        self.context = ContextInterpreter()
        print("🧠 TUYUL-FX Reflex Console v6.0 Ready.")

    def start(self):
        while True:
            user_input = input("💬 You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("👋 Reflective Console closing...")
                break

            ctx = self.context.parse(user_input)
            result = self.chat.chat(user_input)

            print(f"🪞 Context Tone: {ctx['tone']}")
            print(f"🤖 TUYUL: {result['reflective_response']}")
            print(f"⚛️ Coherence: {result['coherence']}")
