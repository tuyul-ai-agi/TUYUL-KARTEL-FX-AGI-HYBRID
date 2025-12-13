#!/bin/bash
# ============================================================
# 🧠 TUYUL FX AGI – Docker Cleanup Utility
# ============================================================

echo "🧹 Membersihkan container & image lama..."
docker container prune -f
docker image prune -a -f
docker volume prune -f
echo "✅ Docker environment TUYUL FX AGI dibersihkan."
