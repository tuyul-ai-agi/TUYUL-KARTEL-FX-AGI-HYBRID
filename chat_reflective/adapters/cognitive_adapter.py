"""
Cognitive Adapter v6.0
-----------------------------------------
Adapts raw text or emotional input into structured
reflective reasoning compatible with TUYUL Cognitive Layer.
"""

from datetime import datetime


class CognitiveAdapter:
    def __init__(self):
        self.history = []

    def encode(self, user_input):
        """Convert natural input into structured reflective token."""
        encoded = {
            "timestamp": datetime.utcnow().isoformat(),
            "input_text": user_input,
            "reflective_tokens": [word.lower() for word in user_input.split()],
        }
        self.history.append(encoded)
        return encoded
