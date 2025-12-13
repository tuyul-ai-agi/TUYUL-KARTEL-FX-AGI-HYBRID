"""
Wolf Reflective Loop
--------------------
Siklus reflektif otomatis untuk memperbarui reasoning dan bias AGI Hybrid.
"""

from core.reflective.relearning_cycle import RelearningCycle
from core.journal.journal_writer_v540 import JournalWriter
from pipeline.quad_repo_sync_loop import quad_repo_sync_loop

class WolfReflectiveLoop:
    def __init__(self):
        self.relearn = RelearningCycle()
        self.journal = JournalWriter()

    def run(self):
        result = self.relearn.execute()
        self.journal.write_entry({
            "type": "reflective_update",
            "result": result
        })
        return {"status": "completed", "details": result}

    def start_quad_repo_sync(self, interval_minutes=10):
        quad_repo_sync_loop(interval_minutes=interval_minutes)


def wolf_reflective_loop(interval_minutes=10):
    print("🐺 Starting WOLF Reflective Supervisor Loop v5.7.8...")
    quad_repo_sync_loop(interval_minutes=interval_minutes)
