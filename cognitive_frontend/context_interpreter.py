"""
Context Interpreter
-------------------
Modul yang menterjemahkan input manusia (bahasa natural)
menjadi perintah AGI Hybrid (Reflex–Fusion–Reflective Command).
"""

import re
from typing import Dict


class ContextInterpreter:
    def __init__(self) -> None:
        self.patterns: Dict[str, str] = {
            r"analisa\s+(\w+)\s+(\w+)": "gas kan analisa {pair} {tf}",
            r"risiko\s+(\d+)": "calculate risk {balance}",
            r"sync\s+vault": "journal trade",
            r"refleksi": "reflective cycle",
        }

    def interpret(self, text: str) -> str:
        """
        Mengubah kalimat alami menjadi perintah AGI formal.
        """

        for pattern, command in self.patterns.items():
            match = re.search(pattern, text.lower())
            if match:
                groups = match.groups()
                if "analisa" in pattern:
                    return command.format(pair=groups[0].upper(), tf=groups[1].upper())
                if "risiko" in pattern:
                    return command.format(balance=groups[0])
        return text
