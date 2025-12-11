#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TUYUL FX AGI HYBRID v5.7.3r++
Reflective Prompt Manifest Builder
-----------------------------------
Author  : TUYUL Labs — Reflective Systems Division
Version : v5.7.3r++
Protocol: RBP v2.2
Date    : 2025-12-11

Fungsi:
  • Membaca overview_prompt_manifest.yml
  • Membuat ulang semua file prompt (.md)
  • Menyisipkan header metadata & template reflektif
  • Digunakan otomatis oleh GitHub Actions / CI bot (tuyulagibot-tjx)
"""

import os, yaml, datetime, textwrap, json

BASE_PATH = "ai_bridge/prompt_templates/"
MANIFEST_FILE = os.path.join(BASE_PATH, "overview_prompt_manifest.yml")

TEMPLATE_HEADER = """---
title: "{title}"
version: "{version}"
author: "TUYUL Labs — Reflective Systems Division"
date: "{date}"
license: "TUYUL LABS INTERNAL USE ONLY"
description: "{description}"
---

# {title}
> "{quote}"

## 🎯 Tujuan
{goal}

## 🧩 Input
{inputs}

## ⚙️ Proses
{process}

## 🧾 Output JSON
```json
{output}
