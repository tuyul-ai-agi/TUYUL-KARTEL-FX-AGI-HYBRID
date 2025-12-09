# ============================================================
# 🧠 TUYUL FX AGI HYBRID v5.7.3r++ — Reflective Container
# ============================================================

FROM python:3.11-slim

LABEL maintainer="TUYUL Labs <dev@tuyulkartel.ai>"
LABEL version="v5.7.3r++"
LABEL description="Reflective Intelligence Hybrid System (Quad Repo Mode)"

WORKDIR /app

# Update and install system deps
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    pip install --upgrade pip setuptools wheel

# Copy source
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose ports for FastAPI / Reflex API
EXPOSE 8080

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8080/health || exit 1

# Default command
CMD ["python", "main.py"]
