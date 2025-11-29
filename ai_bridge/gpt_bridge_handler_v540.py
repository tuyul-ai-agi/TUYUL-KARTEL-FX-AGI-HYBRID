"""
GPT Bridge Handler v5.4.0
-------------------------
Menangani koneksi dan komunikasi antara AGI Hybrid dan model GPT.
"""

import os
import requests
import json
from .gpt_command_parser_v540 import CommandParser
from .gpt_context_memory import ContextMemory


class GPTBridge:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.endpoint = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1/chat/completions")
        self.model = os.getenv("GPT_MODEL", "gpt-5-turbo")
        self.memory = ContextMemory()
        self.parser = CommandParser()

    def send_prompt(self, role: str, prompt: str, temperature=0.4):
        """
        Kirim prompt ke GPT model dan kembalikan hasil reasoning.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": f"You are {role}"},
                {"role": "user", "content": prompt},
            ],
            "temperature": temperature,
            "max_tokens": 4096,
        }
        response = requests.post(self.endpoint, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()["choices"][0]["message"]["content"]

        self.memory.save(role, prompt, result)
        return result

    def execute_reflex(self, text):
        """Proses prompt Reflex Layer"""
        prompt = self.parser.parse_reflex_command(text)
        return self.send_prompt("Reflex Layer", prompt, temperature=0.2)

    def execute_fusion(self, text):
        """Proses prompt Fusion Layer"""
        prompt = self.parser.parse_fusion_command(text)
        return self.send_prompt("Fusion Layer", prompt, temperature=0.4)

    def execute_reflective(self, text):
        """Proses prompt Reflective Layer"""
        prompt = self.parser.parse_reflective_command(text)
        return self.send_prompt("Reflective Layer", prompt, temperature=0.6)
