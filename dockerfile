# 🐺 TUYUL FX AGI HYBRID DOCKERFILE
FROM python:3.10-slim

# 1️⃣ Set working directory
WORKDIR /app

# 2️⃣ Copy project files
COPY . .

# 3️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Expose port
EXPOSE 8080

# 5️⃣ Runtime command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
