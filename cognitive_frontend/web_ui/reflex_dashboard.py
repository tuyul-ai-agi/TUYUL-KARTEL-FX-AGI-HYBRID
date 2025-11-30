"""
Reflex Dashboard WebUI
----------------------
Tampilan visual real-time hasil reasoning Fusion Layer.
Menampilkan CONF12, RCAdj, WLWCI, dan narasi AGI.
"""

import json
from datetime import datetime

import streamlit as st


def launch_reflex_dashboard() -> None:
    st.set_page_config(page_title="🐺 Reflex Dashboard", layout="wide")

    st.title("🧠 Reflex–Fusion Dashboard v5.4.4")
    st.write("Menampilkan status reasoning AGI Hybrid secara real-time ⚡")

    try:
        with open("vaults/fx_vault/fusion_journal.json", encoding="utf-8") as file:
            fusion_data = json.load(file)
    except FileNotFoundError:
        st.warning("Belum ada data fusion_journal.json ditemukan.")
        return

    st.subheader("📊 Fusion Confidence Map")
    st.metric("CONF₁₂", f"{fusion_data.get('conf12', 0):.2f}")
    st.metric("RCAdj", f"{fusion_data.get('rcadj', 0):.2f}")
    st.metric("WLWCI", f"{fusion_data.get('wlwci', 0):.2f}")

    st.write("---")
    st.write(f"🕒 Terakhir diperbarui: {datetime.utcnow().isoformat()} UTC")

    if "fusion_narrative" in fusion_data:
        st.markdown("### 🧩 Narasi AGI:")
        st.info(fusion_data["fusion_narrative"])
