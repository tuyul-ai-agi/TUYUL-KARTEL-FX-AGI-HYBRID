"""
Vault Viewer WebUI
------------------
Menampilkan isi Vault (FX, Kartel, Journal) secara visual.
"""

import json
import os
from typing import Dict, Any

import streamlit as st


def load_vault(vault_path: str) -> Dict[str, Any]:
    if os.path.exists(vault_path):
        with open(vault_path, encoding="utf-8") as file:
            return json.load(file)
    return {}


def launch_vault_viewer() -> None:
    st.set_page_config(page_title="📚 Vault Viewer", layout="wide")
    st.title("📦 TUYUL Hybrid Vault Viewer")

    vault_options = {
        "FX Vault": "vaults/fx_vault/fusion_journal.json",
        "Kartel Vault": "vaults/kartel_vault/fusion_output.json",
        "Journal Vault": "vaults/journal_vault/reflection_output.json",
    }

    vault_choice = st.selectbox("Pilih Vault untuk dilihat:", list(vault_options.keys()))
    data = load_vault(vault_options[vault_choice])

    if not data:
        st.warning("Tidak ada data di vault terpilih.")
        return

    st.json(data)
    st.success(f"✅ Berhasil memuat data dari {vault_choice}")
