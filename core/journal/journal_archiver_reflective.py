# Reflective Journal Archiver — TUYUL FX v5.7.3r++
import datetime
import json
import os
import shutil


class ReflectiveJournalArchiver:
    """Mengarsipkan log reflektif dan menjaga integritas Vault."""

    ARCHIVE_PATH = "journal/archive/"

    def __init__(self):
        os.makedirs(self.ARCHIVE_PATH, exist_ok=True)

    def archive_logs(self):
        """Pindahkan log lama ke folder arsip dengan index reflektif."""
        now = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        source = "journal/vault_reflective_log.json"
        if os.path.exists(source):
            destination = f"{self.ARCHIVE_PATH}vault_reflective_log_{now}.json"
            shutil.move(source, destination)
            print(f"🗃️ Journal archived → {destination}")
            return {"status": "archived", "path": destination}
        return {"status": "no_logs"}

    def index_archive(self):
        """Membangun index dari semua arsip reflektif."""
        index = []
        for file in os.listdir(self.ARCHIVE_PATH):
            if file.endswith(".json"):
                path = os.path.join(self.ARCHIVE_PATH, file)
                size_kb = round(os.path.getsize(path) / 1024, 2)
                index.append({"file": file, "size_kb": size_kb})
        index_path = os.path.join(self.ARCHIVE_PATH, "index.json")
        with open(index_path, "w", encoding="utf-8") as file:
            json.dump(
                {"timestamp": datetime.datetime.utcnow().isoformat(), "files": index},
                file,
                indent=2,
            )
        print(f"📜 Journal archive index updated — {len(index)} entries")
        return index
