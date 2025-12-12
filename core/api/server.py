"""FastAPI server entrypoint for TUYUL FX AGI Hybrid reflective API."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI

from core.api.api_router import ReflectiveAPIRouter

app = FastAPI(title="TUYUL FX Reflective API", version="5.7.3r++", openapi_url="/openapi.json")
app.include_router(ReflectiveAPIRouter)


def run() -> None:
    """Run the reflective API server on port 5526."""

    uvicorn.run("core.api.server:app", host="0.0.0.0", port=5526, reload=False)


if __name__ == "__main__":
    run()
