# 🧩 ReflectiveDashboard — TUYUL FX AGI HYBRID v5.7.3r++
# Auto-launch web dashboard dan CLI secara paralel
import asyncio
from .web_ui import run_reflective_dashboard
from .reflex_console import ReflexConsole

async def launch_dashboard():
    console = ReflexConsole()
    loop_task = asyncio.create_task(asyncio.to_thread(console.start, 30))
    web_task = asyncio.create_task(asyncio.to_thread(run_reflective_dashboard))
    await asyncio.gather(loop_task, web_task)
