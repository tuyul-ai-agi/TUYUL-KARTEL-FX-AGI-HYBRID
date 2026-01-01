"""
Context Interpreter v6.0
-----------------------------------------
Interprets user input into structured reflective context
before being passed to reasoning layers.
"""

import re
from datetime import datetime


class ContextInterpreter:
    def __init__(self):
        self.last_context = None

    def parse(self, user_input):
        """Extract reflective keywords and emotional tone."""
        tone = "neutral"
        if "?" in user_input:
            tone = "curious"
        if "!" in user_input:
            tone = "urgent"
        if "kenapa" in user_input.lower():
            tone = "analytical"

        context = {
            "timestamp": datetime.utcnow().isoformat(),
            "tokens": re.findall(r"\w+", user_input.lower()),
            "tone": tone,
            "length": len(user_input.split()),
        }

        self.last_context = context
        return context
