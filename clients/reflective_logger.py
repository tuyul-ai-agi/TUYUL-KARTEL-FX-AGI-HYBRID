"""
Reflective Logger v6.0
-----------------------------------------
Global reflective event logger used by bridge managers.
"""

import json, os
from datetime import datetime

class ReflectiveLogger:
    def __init__(self, path="logs/reflective_core_log.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def log(self, event, level="INFO"):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "event": event
        }
        data = []
        if os.path.exists(self.path):
            data = json.loads(open(self.path).read() or "[]")
        data.append(entry)
        json.dump(data, open(self.path, "w"), indent=2)
