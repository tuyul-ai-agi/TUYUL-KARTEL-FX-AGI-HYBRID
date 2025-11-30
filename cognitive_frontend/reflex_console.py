"""
Reflex Console
--------------
CLI Interface untuk operator AGI Hybrid.
Menjalankan perintah reflex, fusion, dan reflective reasoning langsung ke GPTBridge.
"""

from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler as GPTBridge
from cognitive_frontend.context_interpreter import ContextInterpreter


class ReflexConsole:
    def __init__(self) -> None:
        self.bridge = GPTBridge()
        self.interpreter = ContextInterpreter()

    def run(self) -> None:
        print("🐺 TUYUL Reflex Console v5.4.4 — siap menerima perintah AGI Boss ⚡")
        print("Ketik 'exit' untuk keluar.\n")

        while True:
            try:
                user_input = input("🧠 > ").strip()
                if user_input.lower() in ["exit", "quit"]:
                    print("Serigala hening... keluar dari mode reflex 🐺")
                    break

                command = self.interpreter.interpret(user_input)
                if command.startswith("gas kan analisa"):
                    _, _, pair, tf = command.split()
                    result = self.bridge.run_analysis(pair, tf)
                    print(f"📊 Hasil Fusion: {result}\n")

                elif command.startswith("calculate risk"):
                    balance = command.split()[-1]
                    print(f"💰 Simulasi risiko untuk balance: {balance} USD (dummy mode)\n")

                elif "reflective cycle" in command:
                    status = self.bridge.get_status()
                    print(f"🔮 Reflective Output (status snapshot): {status}\n")

                elif "journal trade" in command:
                    print("🗃️ Sinkronisasi vault berjalan... (mock mode)\n")

                else:
                    print("⚠️ Perintah tidak dikenali. Coba: 'analisa EURUSD H1' atau 'refleksi'.")

            except KeyboardInterrupt:
                print("\nKeluar dari Reflex Console 🧘‍♂️")
                break
            except Exception as exc:  # pragma: no cover - interactive tool
                print(f"❌ Error: {exc}")
