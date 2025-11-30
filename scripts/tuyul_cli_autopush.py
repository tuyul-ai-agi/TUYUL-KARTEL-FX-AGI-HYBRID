"""
Tuyul CLI Autopush
------------------
Auto-push commit ke GitHub untuk log dan vault reasoning.
"""

import os
import subprocess

if __name__ == "__main__":
    os.system("git add .")
    os.system('git commit -m "Auto update: reasoning log & vault sync"')
    os.system("git push origin main")
    print("🚀 Auto-push complete.")
