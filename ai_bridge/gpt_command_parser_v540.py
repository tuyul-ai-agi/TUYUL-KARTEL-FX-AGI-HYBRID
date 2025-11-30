"""
GPT Command Parser v5.4.0
-------------------------
Parser untuk memetakan input natural language menjadi struktur prompt GPT.
"""

import re


class CommandParser:
    def parse_reflex_command(self, text: str) -> str:
        return f"Analisa cepat pola harga: {text}. Berikan arah bias pasar (BUY/SELL/WAIT)."

    def parse_fusion_command(self, text: str) -> str:
        return f"Gabungkan hasil reflex dan smart money flow: {text}. Hitung CONF12 dan WLWCI."

    def parse_reflective_command(self, text: str) -> str:
        return f"Evaluasi bias dan hasil reasoning berikut: {text}. Berikan rekomendasi meta-learning."
