"""
🐺 TUYUL FX AGI HYBRID – Main Launcher v5.4.1-H
FastAPI runtime utama yang menggabungkan router reflektif & GPT bridge AGI Hybrid.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.central_router import api_router

# ==============================
# ⚙️ Konfigurasi Aplikasi
# ==============================
app = FastAPI(
    title="TUYUL FX AGI HYBRID 🧠🐺",
    description="Reflex–Fusion–Vault–GPT unified orchestrator v5.4.1-H",
    version="5.4.1-H",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ==============================
# 🌐 CORS Policy
# ==============================
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://tuyulwolf.ai",
    "https://tjx578.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 🧩 Router AGI Hybrid
# ==============================
app.include_router(api_router, prefix="/api")

# ==============================
# 🧠 Root Diagnostic
# ==============================
@app.get("/")
async def root():
    return {
        "status": "🧠 TUYUL FX AGI HYBRID aktif",
        "version": "v5.4.1-H",
        "modules": [
            "Fusion",
            "Reflex",
            "Risk",
            "Vault",
            "Reflective",
            "GPT Bridge",
            "System",
        ],
        "sync_state": "Online",
    }

# ==============================
# 🚀 Runtime Entry
# ==============================
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
