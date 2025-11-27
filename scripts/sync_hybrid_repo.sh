#!/usr/bin/env bash
# 🐺 TUYUL-KARTEL-FX-AGI-HYBRID — Hybrid Repo Sync Helper
set -euo pipefail

REPO_SLUG=${REPO_SLUG:-tjx578/TUYUL-KARTEL-FX-AGI-HYBRID}
TARGET_DIR=${TARGET_DIR:-vaults/hybrid_repo}
BRANCH_NAME=${BRANCH_NAME:-main}

if [[ -z "${WOLF_KEY:-}" ]]; then
    echo "❌ WOLF_KEY belum diset di environment."
    echo "Set WOLF_KEY atau ekspor manual sebelum menjalankan sinkronisasi."
    exit 1
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    export GITHUB_TOKEN="$WOLF_KEY"
    echo "🔐 GITHUB_TOKEN diisi otomatis dari WOLF_KEY."
else
    echo "ℹ️ GITHUB_TOKEN sudah tersedia, tidak dioverride."
fi

AUTH_URL="https://${GITHUB_TOKEN}@github.com/${REPO_SLUG}.git"
GIT_TERMINAL_PROMPT=0 git ls-remote -h "$AUTH_URL" HEAD >/dev/null

if [[ -d "$TARGET_DIR/.git" ]]; then
    echo "🔁 Repo sudah ada. Menarik update dari ${BRANCH_NAME}..."
    git -C "$TARGET_DIR" fetch origin
    git -C "$TARGET_DIR" checkout "$BRANCH_NAME"
    git -C "$TARGET_DIR" reset --hard "origin/${BRANCH_NAME}"
else
    echo "📥 Repo belum ada. Melakukan clone ke $TARGET_DIR..."
    git clone --branch "$BRANCH_NAME" "$AUTH_URL" "$TARGET_DIR"
fi

unset AUTH_URL

cat <<MSG
✅ Sinkronisasi selesai.
- Repo: ${REPO_SLUG}
- Target: ${TARGET_DIR}
- Token: GITHUB_TOKEN (bersumber dari WOLF_KEY)

Siap Bossku, hybrid repo sudah sinkron. 🧠⚡
MSG
