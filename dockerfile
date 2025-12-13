# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.8
# Reflective Volatility Cycle Core
# ============================================================

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "main.py"]
