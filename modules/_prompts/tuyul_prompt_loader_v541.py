```python
"""
Tuyul Prompt Loader v5.4.1
--------------------------
Membaca template prompt Markdown dan mengganti placeholder variabel.
"""

import os

class PromptLoader:
    def __init__(self, prompt_dir="_prompts/"):
        self.prompt_dir = prompt_dir

    def load_prompt(self, filename: str, **kwargs):
        path = os.path.join(self.prompt_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt {filename} not found")
        with open(path, "r") as f:
            content = f.read()
        for key, val in kwargs.items():
            content = content.replace(f"{{{{{key}}}}}", str(val))
        return content
