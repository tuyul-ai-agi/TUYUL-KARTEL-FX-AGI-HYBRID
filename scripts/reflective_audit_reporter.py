"""
Reflective Audit Reporter
-------------------------
Membuat laporan audit reasoning dari Journal Vault.
"""

from clients.journal_vault_client import JournalVaultClient
import json

if __name__ == "__main__":
    journal = JournalVaultClient()
    reflections = journal.get_recent_reflections(limit=10)
    with open("logs/reflective_audit_report.json", "w") as f:
        json.dump(reflections, f, indent=2)
    print("📊 Reflective audit report generated: logs/reflective_audit_report.json")
