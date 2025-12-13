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
"""Lightweight command interpreter used by the reflective bot."""

from datetime import datetime
from typing import Callable, Dict


COMMAND_HANDLERS: Dict[str, Callable[[], None]] = {}


def _register(command: str):
    def decorator(func: Callable[[], None]) -> Callable[[], None]:
        COMMAND_HANDLERS[command] = func
        return func

    return decorator


@_register("status_report")
def _status_report() -> None:
    timestamp = datetime.utcnow().isoformat()
    print(f"[BOT] STATUS REPORT @ {timestamp} :: OK")


@_register("resync_repo")
def _resync_repo() -> None:
    timestamp = datetime.utcnow().isoformat()
    print(f"[BOT] RESYNC triggered @ {timestamp}")


@_register("noop")
def _noop() -> None:
    print("[BOT] No-op command executed")


def interpret_command(command: str) -> None:
    handler = COMMAND_HANDLERS.get(command)
    if handler:
        handler()
    else:
        print(f"[BOT] Unknown command: {command}")
