import re


COMMANDS = {
    r"gas kan analisa (\w+) (\w+)": "run_analysis",
    r"calculate risk (\d+)": "calculate_risk",
    r"sync hybrid": "sync_vaults",
    r"reflective cycle": "run_reflection",
}


class GPTCommandParser:
    def parse(self, text: str):
        """Mendeteksi perintah GPT Reflex Command dari input teks pengguna."""
        for pattern, action in COMMANDS.items():
            match = re.search(pattern, text.lower())
            if match:
                args = match.groups()
                return {"command": action, "args": args}
        return {"command": "unknown", "args": ()}
