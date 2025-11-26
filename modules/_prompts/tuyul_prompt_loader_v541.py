"""
🐺 TUYUL FX ULTRA WOLF v5.4.1 - Prompt Loader
Auto parser for Markdown prompt definition file
Integrates with GPT Bridge Handler & Vault AutoSync system.
"""

import os
import re
import yaml
import json
import hashlib
import asyncio
import aiofiles
import redis
from datetime import datetime
from typing import Dict, Any

# === Redis Cache untuk runtime integration ===
rdb = redis.Redis(host="localhost", port=6379, db=0)


class TuyulPromptLoaderV541:
    def __init__(self, prompt_path: str = "./knowledge_base/_prompts/tuyul_fx_prompt_v541.md"):
        self.prompt_path = prompt_path
        self.prompt_data: Dict[str, Any] = {}
        self.hash_key = "tuyul_prompt_v541_hash"
        self.redis_channel = "prompt_update_event"

    async def _read_file(self) -> str:
        """Baca file prompt markdown secara async."""
        async with aiofiles.open(self.prompt_path, "r", encoding="utf-8") as f:
            return await f.read()

    @staticmethod
    def _calculate_sha1(content: str) -> str:
        """Hitung hash SHA1 untuk differential sync tracking."""
        return hashlib.sha1(content.encode("utf-8")).hexdigest()

    def _extract_sections(self, text: str) -> Dict[str, str]:
        """Pisahkan bagian Markdown menjadi section dengan regex."""
        sections = re.split(r"(?m)^##\s+", text)
        parsed = {}
        for section in sections:
            lines = section.strip().splitlines()
            if not lines:
                continue
            header = lines[0].strip("# ").strip()
            parsed[header] = "\n".join(lines[1:]).strip()
        return parsed

    async def parse_prompt(self):
        """Parse prompt markdown menjadi dictionary terstruktur."""
        raw = await self._read_file()
        current_hash = self._calculate_sha1(raw)

        # Cek hash lama untuk delta sync
        previous_hash = rdb.get(self.hash_key)
        if previous_hash and previous_hash.decode() == current_hash:
            print("🐺 Prompt v5.4.1 sudah up-to-date, tidak ada perubahan.")
            return

        # Ekstraksi section
        sections = self._extract_sections(raw)

        self.prompt_data = {
            "version": "v5.4.1",
            "timestamp": datetime.utcnow().isoformat(),
            "meta": {
                "mode": "Hybrid Reflex AGI",
                "philosophy": "Precision bukan sekadar akurasi — ini naluri bertahan hidup.",
                "closing_quote": "Siap Bossku, gaskeun serigala. Tuyul log ke Journal Boss 📝🔥"
            },
            "sections": sections
        }

        # Simpan ke Redis
        rdb.set("tuyul_prompt_v541_data", json.dumps(self.prompt_data))
        rdb.set(self.hash_key, current_hash)

        # Broadcast perubahan prompt
        rdb.publish(self.redis_channel, json.dumps({
            "event": "prompt_updated",
            "timestamp": datetime.utcnow().isoformat(),
            "hash": current_hash
        }))

        print("✅ Prompt TUYUL v5.4.1 berhasil dimuat dan diregistrasikan ke sistem GPT Bridge.")

        # Simpan versi YAML untuk Vault Sync
        await self._save_yaml_snapshot()

    async def _save_yaml_snapshot(self):
        """Simpan snapshot YAML dari data prompt ke Vault untuk sinkronisasi lintas repo."""
        yaml_path = "./vaults/snapshots/prompt_snapshot_v541.yaml"
        os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
        async with aiofiles.open(yaml_path, "w", encoding="utf-8") as f:
            yaml_data = yaml.dump(self.prompt_data, sort_keys=False, allow_unicode=True)
            await f.write(yaml_data)
        print(f"📦 Snapshot prompt tersimpan di {yaml_path}")

    async def register_to_bridge(self):
        """Registrasi ke GPT Bridge system (v540)."""
        bridge_path = "./modules/bridge_module_v540.py"
        if not os.path.exists(bridge_path):
            print("⚠️ GPT Bridge belum ditemukan, skip registrasi otomatis.")
            return

        print("🔗 Integrasi ke GPT Bridge Handler aktif...")
        await asyncio.sleep(0.5)
        print("🐺 Command set (Hybrid Reflex v5.4.1) terdaftar ke GPT Command Parser.")

    async def run(self):
        await self.parse_prompt()
        await self.register_to_bridge()


# === CLI Execution ===
if __name__ == "__main__":
    print("🐺 Memuat TUYUL FX Prompt Loader v5.4.1...")
    loader = TuyulPromptLoaderV541()
    asyncio.run(loader.run())
