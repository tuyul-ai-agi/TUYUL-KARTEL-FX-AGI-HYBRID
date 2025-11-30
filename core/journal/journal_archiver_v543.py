"""
Journal Archiver v5.4.3
-----------------------
Mengarsipkan log lama Journal Vault ke ZIP.
"""

import os
import zipfile
from datetime import datetime


class JournalArchiver:
    def __init__(self, vault_path="vaults/journal_vault/archives/"):
        self.vault_path = vault_path
        os.makedirs(self.vault_path, exist_ok=True)

    def archive(self, target_dir="vaults/journal_vault/"):
        archive_name = f"journal_archive_{datetime.utcnow().strftime('%Y%m%d')}.zip"
        archive_path = os.path.join(self.vault_path, archive_name)

        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(target_dir):
                for file in files:
                    if file.endswith(".json"):
                        full_path = os.path.join(root, file)
                        zipf.write(full_path, os.path.relpath(full_path, target_dir))
        return {"archive": archive_name, "status": "archived"}
