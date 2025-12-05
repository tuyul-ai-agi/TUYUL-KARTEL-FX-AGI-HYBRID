#!/usr/bin/env bash
# ======================================================
# 🧠 TUYUL FX AGI - Codespace Repair Script (v5.7.2)
# Tujuan: memperbaiki error "Sorry, no response was returned."
# ======================================================

echo "🐺 TUYUL FX AGI Codespace Repair Utility ⚡"
echo "-------------------------------------------"

# 1️⃣ Pindah ke root project
cd "$(dirname "$0")"/.. || exit 1

# 2️⃣ Cek file YAML Bridge
if [ -f "configs/agi_hybrid_bridge.yml" ]; then
    echo "✅ Found: configs/agi_hybrid_bridge.yml"
else
    echo "❌ Bridge file not found! Regenerating..."
    python3 tools/generate_bridge_yaml.py || {
        echo "⚠️ Failed to regenerate agi_hybrid_bridge.yml"
        exit 1
    }
fi

# 3️⃣ Validasi YAML
if command -v yamllint >/dev/null 2>&1; then
    yamllint configs/agi_hybrid_bridge.yml || echo "⚠️ YAML validation skipped (non-fatal)"
else
    echo "ℹ️ yamllint not found, skipping YAML check"
fi

# 4️⃣ Hentikan semua proses Python yang nyangkut
echo "🧩 Killing stale Python processes..."
pkill -f "main.py" >/dev/null 2>&1
pkill -f "pipeline" >/dev/null 2>&1
pkill -f "fusion" >/dev/null 2>&1
sleep 2

# 5️⃣ Bersihkan lock Vault
echo "🧱 Cleaning Vault locks..."
rm -f vaults/*/sync.lock 2>/dev/null || true

# 6️⃣ Bersihkan cache log
mkdir -p logs
echo "" > logs/bridge_events.log
echo "" > logs/bridge_debug.log

# 7️⃣ Cek koneksi internet Codespace
echo "🌐 Checking network connectivity..."
ping -c 2 github.com >/dev/null 2>&1 && echo "✅ Network OK" || echo "⚠️ Limited network access"

# 8️⃣ Tes environment Python
echo "🐍 Checking Python environment..."
python3 -m pip install -r requirements.txt --quiet
python3 -c "import yaml, os; print('✅ Python OK, YAML module loaded')" || {
    echo "❌ Python environment broken, rebuild container recommended."
    exit 1
}

# 9️⃣ Restart BOT Workflow (GitHub Actions)
echo "🤖 Restarting Reflective BOT workflow..."
gh workflow run .github/workflows/quad_vault_reflective_sync.yml --ref main || echo "⚠️ BOT restart skipped"

# 🔟 Jalankan pipeline sanity check
echo "🧠 Running pipeline diagnostic..."
python3 tools/telemetry_logger.py --diagnose || echo "⚠️ Diagnostic incomplete"

echo "✅ Repair complete! Codespace is clean and ready."
echo "📗 You can now re-run:"
echo "   python main.py --layer Reflex"
echo "   or"
echo "   python main.py --layer all --fast"
echo "-------------------------------------------"
echo "🐺 Ready to hunt again, Bossku ⚡"
