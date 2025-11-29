"""
Vault AutoSync v5.4.1
---------------------
Sinkronisasi otomatis antara FX Vault, Kartel Vault, dan Journal Vault.
"""

import os
import requests
import json


class VaultAutoSync:
    def __init__(self):
        self.fx_url = os.getenv("FX_VAULT_BASE_URL")
        self.kartel_url = os.getenv("KARTEL_VAULT_BASE_URL")
        self.journal_url = os.getenv("JOURNAL_VAULT_BASE_URL")

    def sync_all(self):
        print("🔗 Syncing Vaults: FX ↔ Kartel ↔ Journal")
        fx = requests.get(f"{self.fx_url}/sync").status_code
        kartel = requests.get(f"{self.kartel_url}/sync").status_code
        journal = requests.get(f"{self.journal_url}/sync").status_code
        return {"fx": fx, "kartel": kartel, "journal": journal}
