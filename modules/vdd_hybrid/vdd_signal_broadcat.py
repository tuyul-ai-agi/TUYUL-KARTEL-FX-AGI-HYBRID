import json
from datetime import datetime

class VDDBroadcast:
    """
    Publikasi sinyal rezim ke modul lain.
    """
    def __init__(self):
        pass

    def broadcast(self, state: int, probabilities: list):
        payload = {
            "RegimeState": state,
            "Probabilities": probabilities,
            "Timestamp": datetime.utcnow().isoformat()
        }
        print(json.dumps(payload))  # Redis publish bisa ditambahkan di sini
        return payload
