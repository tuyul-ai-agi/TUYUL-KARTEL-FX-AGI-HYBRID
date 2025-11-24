"""Command parser for GPT reflex commands."""

import re
from typing import Any, Dict, Tuple


COMMANDS = {
    r"gas kan analisa (\w+) (\w+)": "run_analysis",
    r"calculate risk (\d+)": "calculate_risk",
    r"sync hybrid": "sync_vaults",
    r"reflective cycle": "run_reflection",
}


class GPTCommandParser:
    """Parser for natural language commands to system actions."""
    
    def parse(self, text: str) -> Dict[str, Any]:
        """Detect and parse GPT Reflex Commands from user input.
        
        Args:
            text: User input text to parse.
            
        Returns:
            Dictionary with command name and extracted arguments.
        """
        for pattern, action in COMMANDS.items():
            match = re.search(pattern, text.lower())
            if match:
                args = match.groups()
                return {"command": action, "args": args}
        return {"command": "unknown", "args": ()}
