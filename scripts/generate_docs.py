"""
Generate Docs
-------------
Auto-generate dokumentasi modul ke folder docs/.
"""

import os

def generate_docs(src_dir="core", output="docs/module_index.md"):
    with open(output, "w") as f:
        for root, _, files in os.walk(src_dir):
            for file in files:
                if file.endswith(".py"):
                    f.write(f"- {os.path.join(root, file)}\n")
    print(f"✅ Docs generated: {output}")

if __name__ == "__main__":
    generate_docs()
