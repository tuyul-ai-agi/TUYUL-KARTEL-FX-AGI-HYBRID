# ============================================================
# 🧠 TUYUL-KARTEL-FX AGI HYBRID v5.8r+
# File: Dockerfile
# ------------------------------------------------------------
# Multi-stage build container untuk Reflective Quad Repo System
# Base OS: Debian (Python 3.11)
# Mode: Reflective Discipline (Production)
# ============================================================

# ============================================================
# 🔹 1️⃣ STAGE — BUILDER (Install dependencies)
# ============================================================
FROM python:3.11-slim AS builder

LABEL maintainer="TUYUL-LABS"
LABEL description="Reflective AGI Hybrid Build Environment"

WORKDIR /app
ENV PIP_NO_CACHE_DIR=1

# Instalasi package dasar & dev tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    git \
    curl \
    wget \
    ca-certificates \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Pasang dependensi Python
COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel && \
    pip install --prefix=/install -r requirements.txt

# Copy semua file proyek
COPY . .

# ============================================================
# 🔹 2️⃣ STAGE — RUNTIME (Production)
# ============================================================
FROM python:3.11-slim AS runtime

ENV TZ=Asia/Jakarta \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependensi runtime minimal
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy hasil build dari stage sebelumnya
COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# Buat folder log dan repo jika belum ada
RUN mkdir -p /app/logs /app/journal_repo /app/knowledge /app/configs

# Healthcheck default
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:8000/bridge/status || exit 1

# ============================================================
# 🔹 3️⃣ ENTRYPOINT REFLECTIVE HYBRID
# ============================================================
# Default entry akan dibaca dari manifest atau override compose
ENTRYPOINT ["python", "main.py"]

# ============================================================
# 🔹 4️⃣ LABELING METADATA
# ============================================================
LABEL org.tuyul.version="v5.8r+" \
      org.tuyul.repo="TUYUL-KARTEL-FX" \
      org.tuyul.mode="Quad Repo Reflective" \
      org.tuyul.bridge_protocol="RBP_v2.2" \
      org.tuyul.personality="Alpha Serigala Reflective Discipline"

# ============================================================
# 🔹 5️⃣ EXPOSE PORTS
# ============================================================
EXPOSE 8000
EXPOSE 6379

# ============================================================
# 🔹 6️⃣ RUN VALIDATION (Optional, Debug Mode)
# ============================================================
# Uncomment baris di bawah jika ingin testing otomatis startup
# CMD ["python", "bridge_observer_v573r.py"]
