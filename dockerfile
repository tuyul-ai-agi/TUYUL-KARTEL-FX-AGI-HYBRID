# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.8
# Reflective Volatility Cycle Core
# ============================================================

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]
