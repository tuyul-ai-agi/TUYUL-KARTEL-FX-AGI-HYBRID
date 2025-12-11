# ⚡ ReflexConsole — TUYUL FX AGI HYBRID v5.7.3r++
# CLI Realtime Monitoring untuk Reflex–Fusion–Reflective Loop
import time, os
from .context_interpreter import ContextInterpreter

class ReflexConsole:
    def __init__(self):
        self.interpreter = ContextInterpreter()

    def start(self, interval=30):
        os.system("cls" if os.name == "nt" else "clear")
        print("🐺 TUYUL FX AGI HYBRID — Reflex Console v5.7.3r++")
        print("────────────────────────────────────────────")
        while True:
            ctx = self.interpreter.interpret_context()
            os.system("cls" if os.name == "nt" else "clear")
            print(ctx)
            print(f"🕒 Updated every {interval}s — Press Ctrl+C to stop.")
            time.sleep(interval)
