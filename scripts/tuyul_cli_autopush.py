# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – CLI AutoPush BOT
# ============================================================

import os


def autopush(commit_msg: str = "Reflective update"):
    print("🐺 AutoPush Reflective Repo Changes to GitHub...")
    os.system("git add .")
    os.system(f'git commit -m "{commit_msg}"')
    os.system("git push origin main")
    print("✅ AutoPush Complete.")


if __name__ == "__main__":
    autopush()
