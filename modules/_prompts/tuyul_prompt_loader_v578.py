"""
TUYUL FX v5.7.8 - Reflective Prompt Loader
------------------------------------------
Memuat prompt reflektif sesuai versi dan mode sistem.
Memastikan integritas, kompatibilitas, dan metadata prompt.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Union

PROMPT_DIR = Path(__file__).resolve().parent


def _timestamp() -> str:
    """Return UTC ISO8601 timestamp with Z suffix."""
    return datetime.utcnow().isoformat() + "Z"


def load_prompt(name: str) -> Dict[str, Union[str, dict]]:
    """Membaca prompt reflektif (.md) beserta metadata-nya."""
    target = PROMPT_DIR / f"{name}.md"
    if not target.exists():
        return {
            "status": "error",
            "message": f"Prompt {name} tidak ditemukan.",
            "loaded_at": _timestamp(),
        }

    content = target.read_text(encoding="utf-8")
    metadata = {
        "prompt_name": name,
        "version": "v5.7.8",
        "reflective_mode": "HYBRID_BALANCE",
        "timestamp_loaded": _timestamp(),
        "dependencies": ["Fusion", "Reflex", "Reflective", "HybridBalance"],
    }

    print(f"Loaded Reflective Prompt: {name} | Mode=Hybrid Balance")
    return {"status": "ok", "metadata": metadata, "content": content}


def list_prompts(include_legacy: bool = False) -> List[str]:
    """Menampilkan daftar prompt reflektif yang tersedia."""
    names = [p.stem for p in PROMPT_DIR.glob("*.md")]
    if include_legacy:
        legacy_dir = PROMPT_DIR / "legacy"
        names.extend(p.stem for p in legacy_dir.glob("*.md"))
    return sorted(names)


if __name__ == "__main__":
    print("TUYUL Reflective Prompt Loader v5.7.8")
    available = list_prompts()
    print(f"Available Prompts: {available}")
    prompt = load_prompt("tuyul_fx_prompt_v578")
    if prompt.get("status") == "ok":
        print("Metadata:")
        print(prompt["metadata"])
    else:
        print(prompt.get("message"))
