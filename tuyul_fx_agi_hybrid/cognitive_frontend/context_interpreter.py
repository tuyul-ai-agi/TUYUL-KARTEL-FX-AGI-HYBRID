"""Interpreter converting natural language input into system actions."""

from ..core.ai_bridge.gpt_command_parser_v540 import GPTCommandParser
from ..core.hybrid_reflector import run_hybrid_reflection


def interpret_context(user_input: str):
    """Interpret user input and run hybrid reflection when applicable."""

    parser = GPTCommandParser()
    result = parser.parse(user_input)
    if result["command"] == "run_analysis":
        pair, timeframe = result["args"]
        return run_hybrid_reflection(pair, timeframe)
    return {"error": "unknown command"}
