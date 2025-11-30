#!/bin/bash
# Docker Cleanup Utility
# ----------------------
# Membersihkan container, image, dan volume lama dari environment AGI Hybrid.

echo "🧹 Cleaning up old Docker containers and images..."

docker container prune -f
docker image prune -a -f
docker volume prune -f
docker system prune -a -f --volumes

echo "✅ Docker cleanup completed."
