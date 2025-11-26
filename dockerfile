# 🐺 TUYUL FX ULTRA WOLF AGI HYBRID – Dockerfile v5.4.1
# Precision = Survival.

FROM python:3.11-slim

LABEL maintainer="Tuyul Kartel FX AGI Team"
LABEL version="5.4.1"
LABEL description="TUYUL FX ULTRA WOLF AGI HYBRID Runtime Environment"

# =====================================================
# 🔧 SYSTEM PREP
# =====================================================
RUN apt-get update && apt-get install -y \
    git curl build-essential libssl-dev libffi-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

# =====================================================
# 📦 PROJECT SETUP
# =====================================================
WORKDIR /app

# Copy requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Expose API port
EXPOSE 5400

# =====================================================
# 🧠 STARTUP COMMAND
# =====================================================
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5400", "--log-level", "info"]
