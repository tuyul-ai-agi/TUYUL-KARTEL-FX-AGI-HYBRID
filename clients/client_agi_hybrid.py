"""
AGI Hybrid Client v6.0
-----------------------------------------
Communicates with external AGI reflection endpoints.
"""

import requests

class AGIHybridClient:
    def __init__(self, endpoint="http://localhost:8008/reflective/chat"):
        self.endpoint = endpoint

    def send(self, message, user="system"):
        res = requests.post(self.endpoint, json={"message": message, "user": user})
        return res.json()
