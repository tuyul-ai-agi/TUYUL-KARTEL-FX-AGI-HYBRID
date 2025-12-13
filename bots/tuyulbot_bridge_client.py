"""Helper utilities for the TUYUL reflective bot bridge."""

import json
import random
from datetime import datetime
from typing import Any, Dict

import redis


def _redis_client() -> redis.Redis:
    return redis.Redis(host="localhost", port=6379, decode_responses=True)


def publish_event(channel: str, packet: Dict[str, Any]) -> None:
    """Publish an event packet to a Redis channel."""
    client = _redis_client()
    client.publish(channel, json.dumps(packet))


def read_vault_integrity() -> float:
    """Return a simulated vault integrity score between 0 and 1."""
    integrity = round(random.uniform(0.85, 0.99), 2)
    _redis_client().set("vault_integrity", integrity)
    _redis_client().set("vault_integrity_timestamp", datetime.utcnow().isoformat())
    return integrity
