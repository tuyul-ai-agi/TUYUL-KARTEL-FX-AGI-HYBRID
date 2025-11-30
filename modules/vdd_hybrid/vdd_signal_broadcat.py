"""
VDD Signal Broadcaster
----------------------
Broadcast hasil deteksi rezim ke modul lain (Fusion, Reflex, Risk).
"""

class VDDSignalBroadcaster:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, module_name: str):
        self.subscribers.append(module_name)

    def broadcast(self, regime_state: str):
        for sub in self.subscribers:
            print(f"[VDD] → {sub} notified: Regime = {regime_state}")
        return {"subscribers": self.subscribers, "state": regime_state}
