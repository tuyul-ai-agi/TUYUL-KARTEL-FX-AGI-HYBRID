"""CLI for executing Reflex commands manually."""

from ai_bridge.gpt_bridge_handler_v540 import GPTBridgeHandler
from ai_bridge.gpt_command_parser_v540 import GPTCommandParser


def start_console() -> None:
    """Start interactive Reflex console session."""

    parser = GPTCommandParser()
    bridge = GPTBridgeHandler()
    while True:
        cmd = input("T🐺 > ")
        if cmd.lower() in ["exit", "quit"]:
            break
        result = parser.parse(cmd)
        if result["command"] == "run_analysis":
            pair, timeframe = result["args"]
            output = bridge.run_analysis(pair, timeframe)
            print(
                f"CONF₁₂={output['conf12']} | WLWCI={output['wlwci']} | RCAdj={output['rcadj']}"
            )
        else:
            print("⚠️ Command tidak dikenali.")
