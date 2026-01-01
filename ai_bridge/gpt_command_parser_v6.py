"""
GPT Command Parser v6.0
-----------------------------------------
Parses reflective 'thinking' commands and routes them to the appropriate subsystems.
"""


class GPTCommandParser:
    def parse(self, command: str) -> dict:
        lowered = command.lower()
        if "reflect" in lowered:
            return {"action": "run_reflective_cycle"}
        if "sync" in lowered:
            return {"action": "vault_sync"}
        if "observe" in lowered:
            return {"action": "bridge_observe"}
        return {"action": "unknown"}
