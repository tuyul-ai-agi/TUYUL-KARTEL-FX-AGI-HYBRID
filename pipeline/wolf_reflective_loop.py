"""Wolf Reflective Loop.

Siklus reflektif otomatis untuk memperbarui reasoning dan bias AGI Hybrid.
"""

from core.journal.journal_writer_v540 import JournalWriter
from core.reflective.relearning_cycle import RelearningCycle
from pipeline.quad_repo_sync_loop import QuadRepoSyncLoop, quad_repo_sync_loop


class WolfReflectiveLoop:
    def __init__(self):
        self.repo_sync = QuadRepoSyncLoop()
        self.relearn = RelearningCycle()
        self.journal = JournalWriter()

    def run(self) -> dict:
        sync_result = self.repo_sync.run()
        result = self.relearn.execute()
        self.journal.write_entry(
            {
                "type": "reflective_update",
                "sync": sync_result,
                "result": result,
            }
        )
        return {"status": "completed", "sync": sync_result, "details": result}

    def start_quad_repo_sync(self, interval_minutes: int = 10) -> None:
        quad_repo_sync_loop(interval_minutes=interval_minutes)


def wolf_reflective_loop(interval_minutes: int = 10) -> None:
    print("🐺 Starting WOLF Reflective Supervisor Loop v5.7.8...")
    quad_repo_sync_loop(interval_minutes=interval_minutes)
