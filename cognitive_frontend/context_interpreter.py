"""Interpreter converting natural language input into system actions."""

from typing import Dict, Any

from ai_bridge.gpt_command_parser_v540 import GPTCommandParser
from ..core.hybrid_reflector import run_hybrid_reflection


def interpret_context(user_input: str) -> Dict[str, Any]:
    """Interpret user input and execute appropriate system actions.
    
    Args:
        user_input: Natural language command from user.
        
    Returns:
        Dictionary with analysis results or error message.
    """
    parser = GPTCommandParser()
    result = parser.parse(user_input)
    if result["command"] == "run_analysis":
        pair, timeframe = result["args"]
        return run_hybrid_reflection(pair, timeframe)
    return {"error": "unknown command"}
