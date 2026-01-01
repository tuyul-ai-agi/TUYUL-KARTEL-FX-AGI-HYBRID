"""
Gemini Bridge v6.0 — TUYUL-FX Quantum Hybrid
---------------------------------------------
Handles communication between the Reflective Chat Layer and
Google Gemini generative models via REST API.

Supports adaptive reflective prompts, temperature modulation,
and awareness synchronization feedback.
"""
import os
import json
from datetime import datetime
from typing import Optional

import requests


class GeminiBridge:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.endpoint = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            "gemini-pro:generateContent"
        )
        self.headers = {"Content-Type": "application/json"}

    def query(self, prompt: str) -> str:
        """Send reflective prompt to Gemini model."""
        payload = {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "topP": 0.9},
        }
        params = {"key": self.api_key}
        try:
            resp = requests.post(
                self.endpoint, headers=self.headers, params=params, json=payload, timeout=15
            )
            if resp.status_code == 200:
                data = resp.json()
                text = (
                    data.get("candidates", [{}])[0]
                    .get("content", {})
                    .get("parts", [{}])[0]
                    .get("text", "")
                )
                self._log_reflection(prompt, text)
                return text
            err = f"Gemini API Error {resp.status_code}: {resp.text}"
            self._log_reflection(prompt, err)
            return f"[Error Reflecting] {err}"
        except Exception as exc:  # pragma: no cover - network failure path
            err = f"Gemini API Exception: {exc}"
            self._log_reflection(prompt, err)
            return f"[Error Reflecting] {err}"

    def _log_reflection(self, prompt: str, output: str) -> None:
        """Logs each reflective interaction."""
        log_path = "chat_reflective/logs/chat_reflective_log.json"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt[:150],
            "response": output[:150],
        }
        try:
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as f:
                    data = json.loads(f.read() or "[]")
            else:
                data = []
        except json.JSONDecodeError:
            data = []
        data.append(entry)
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
