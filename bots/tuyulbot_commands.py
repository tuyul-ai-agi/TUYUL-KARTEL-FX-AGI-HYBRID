"""Command interpreter for TUYULBOT reflective listener."""

from typing import Dict

DEFAULT_RESPONSE = {
    "action": "noop",
    "desc": "Perintah tidak dikenali. Tidak ada aksi diambil.",
}

COMMAND_MAP = {
    "sync all": {
        "action": "sync_all",
        "desc": "Menjalankan sinkronisasi penuh Quad Repo",
    },
    "vault sync": {
        "action": "vault_sync",
        "desc": "Menjalankan sinkronisasi vault utama",
    },
    "journal flush": {
        "action": "journal_flush",
        "desc": "Mem-flush journal dan mengkomit perubahan",
    },
}


def interpret_command(command_text: str) -> Dict[str, str]:
    """Interpret reflective command text into a structured action."""
    if not isinstance(command_text, str):
        return DEFAULT_RESPONSE

    normalized = command_text.strip().lower()
    return COMMAND_MAP.get(normalized, DEFAULT_RESPONSE)
