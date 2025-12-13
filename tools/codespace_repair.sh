#!/bin/bash
# ============================================================
# 🧠 TUYUL FX AGI – Codespace Repair Utility
# ============================================================

echo "🔧 Memulai perbaikan environment Codespace TUYUL FX AGI..."
sudo apt update && sudo apt upgrade -y
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo "✅ Environment diperbaiki dan dependensi diperbarui."
