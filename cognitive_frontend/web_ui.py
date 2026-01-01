"""
Cognitive Web UI Server v6.0
-----------------------------------------
Hosts the reflective dashboard and chat visualization
for TUYUL-FX Quantum Hybrid System.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from clients.reflective_diagnostics import ReflectiveDiagnostics

app = FastAPI(title="TUYUL-FX Cognitive WebUI v6.0")
app.mount("/static", StaticFiles(directory="cognitive_frontend/web_ui/static"), name="static")

templates = Jinja2Templates(directory="cognitive_frontend/web_ui/templates")
diag = ReflectiveDiagnostics()


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    coherence = diag.check_coherence()
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "title": "TUYUL-FX Reflective Dashboard",
            "coherence": coherence,
        },
    )
