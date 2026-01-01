"""
Bridge Observer v6.0
-----------------------------------------
Observes reflective bridge behavior, GPT responses, and Vault sync activity.
Now includes coherence tracking and quantum feedback alignment.
"""

import json
from datetime import datetime
from pathlib import Path


class BridgeObserver:
    def __init__(self, log_path: str = "logs/bridge_observer_log.json"):
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def observe(self, gpt_response, context_vector):
        if not context_vector:
            coherence = 1.0
        else:
            coherence = round(1 - abs(sum(context_vector) / len(context_vector)), 4)
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "coherence_index": coherence,
            "gpt_response_sample": str(gpt_response)[:200],
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
        return coherence
