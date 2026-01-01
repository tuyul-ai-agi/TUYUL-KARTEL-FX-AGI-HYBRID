"""
TUYUL-FX Quantum Hybrid Reflective Bots
Version: v6.0.0
-----------------------------------------
This package hosts all reflective bot instances (AGI, Bridge, Observer).
Each bot runs within a reflective context and communicates via the
Neural Bridge & Quantum Feedback Layer.
"""

__version__ = "6.0.0"
__bots__ = ["tuyulagibot-tjx", "tuyulagibot_reflective"]
__bridge_mode__ = "Quantum-Neural"

from .tuyulagibot-tjx import TuyulagibotTjx
from .tuyulagibot_reflective import TuyulagibotReflective
from .tuyulbot_bridge_client import TuyulbotBridgeClient
from .tuyulbot_commands import TuyulbotCommands
from .tuyulbot_event_listener import TuyulbotEventListener

bots = {
    "tuyulagibot-tjx": TuyulagibotTjx,
    "tuyulagibot_reflective": TuyulagibotReflective,
}

def get_bot_instance(bot_name):
    bot_class = bots.get(bot_name)
    if bot_class:
        return bot_class()
    else:
        raise ValueError(f"Bot {bot_name} not found.")
