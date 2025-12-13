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
