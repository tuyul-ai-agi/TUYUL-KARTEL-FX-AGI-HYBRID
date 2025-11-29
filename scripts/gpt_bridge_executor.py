"""
GPT Bridge Executor
-------------------
Menjalankan GPT Bridge untuk reasoning Reflex/Fusion.
"""

from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler

if __name__ == "__main__":
    handler = GPTBridgeHandler()
    response = handler.run_prompt(pair="XAUUSD", tf="H1", mode="fusion")
    print(response)
