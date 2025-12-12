# 🧠 TUYUL FX AGI HYBRID v5.7.3r++
# Reflective Dataset Validator Dockerfile
# ----------------------------------------
# Lightweight REST/CLI service untuk Sample Data Validator (RBP v2.2)

FROM python:3.10-slim

LABEL maintainer="Tuyul Kartel AGI Core Team"
LABEL version="5.7.3r++"
LABEL description="Reflective Dataset Validator API (RBP v2.2)"

WORKDIR /app

# Install system deps (curl for healthcheck) and clean
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and sample data
COPY core ./core
COPY data ./data

# Expose FastAPI port
EXPOSE 8080

# Environment
ENV PYTHONUNBUFFERED=1
ENV REFLECTIVE_PROTOCOL="RBP v2.2"
ENV SYSTEM_VERSION="v5.7.3r++"

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8080/health || exit 1

# Entrypoint for FastAPI (Uvicorn)
CMD ["uvicorn", "core.utils.reflective_api:app", "--host", "0.0.0.0", "--port", "8080"]
