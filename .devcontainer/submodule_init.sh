#!/usr/bin/env bash
echo "🔄 Menginisialisasi submodule Vault..."

git submodule update --init --recursive || echo "⚠️ Tidak ada submodule ditemukan."
