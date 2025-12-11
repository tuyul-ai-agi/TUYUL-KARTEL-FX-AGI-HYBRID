# 🌐 web_ui.py — TUYUL FX AGI HYBRID v5.7.3r++
# Adaptive Reflective Dashboard via FastAPI + Plotly
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json, os, plotly.graph_objs as go

app = FastAPI(title="TUYUL FX AGI Reflective Dashboard v5.7.3r++")

def load_diagnostics():
    path = "logs/reflective_diagnostics.json"
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)[-50:]

@app.get("/", response_class=HTMLResponse)
def reflective_dashboard():
    data = load_diagnostics()
    if not data:
        return "<h3>❌ No diagnostic data found</h3>"

    timestamps = [d["timestamp"] for d in data]
    reflection_scores = [d["reflection_score"] for d in data]
    integrity = [d["avg_integrity"] for d in data]
    drift = [d["drift"] for d in data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=reflection_scores, mode="lines+markers", name="Reflection Score"))
    fig.add_trace(go.Scatter(x=timestamps, y=integrity, mode="lines", name="Integrity Index"))
    fig.add_trace(go.Bar(x=timestamps, y=drift, name="Bias Drift"))

    fig.update_layout(
        title="🧠 TUYUL Reflective Diagnostics — RBP v2.2",
        xaxis_title="Timestamp",
        yaxis_title="Metrics",
        template="plotly_dark",
        legend=dict(bgcolor="rgba(0,0,0,0)")
    )

    html = fig.to_html(full_html=False, include_plotlyjs="cdn")
    return f"<h2>🧩 TUYUL FX AGI HYBRID Dashboard v5.7.3r++</h2>{html}<hr><small>Reflective Sync Active | TUYUL Labs ©2025</small>"

def run_reflective_dashboard():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5733)
