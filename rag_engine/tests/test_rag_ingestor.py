#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 TUYUL FX AGI HYBRID — Neurotech RAG Ingestor Test Suite
----------------------------------------------------------
Modul pengujian otomatis untuk sistem RAG reflektif TUYUL-KARTEL-FX.
Memastikan integrasi semantic ingestion berjalan mulus.
"""

import json
from pathlib import Path

import numpy as np
import yaml
from sentence_transformers import SentenceTransformer

# === Parameter Path ===
BASE_DIR = Path(__file__).resolve().parents[2]
INGESTOR_PATH = BASE_DIR / Path(
    "rag_engine/knowledge_ingestion/optimized_neurotech_ingestor.py"
)
YAML_PATH = BASE_DIR / "configs/rag_ingest_neurotech.yml"
OUTPUT_JSON = BASE_DIR / Path("vaults/knowledge_base/neurotech_knowledge_base.json")

# === Load Model (untuk validasi embedding) ===
model = SentenceTransformer("all-mpnet-base-v2")


def test_yaml_integrity():
    """Verifikasi struktur pipeline YAML."""

    print("📄 Memeriksa konfigurasi YAML...")
    assert INGESTOR_PATH.exists(), "❌ Modul ingestion tidak ditemukan!"
    assert YAML_PATH.exists(), "❌ File YAML pipeline tidak ditemukan!"
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)
    assert "pipeline" in data, "❌ Struktur YAML tidak valid!"
    assert data["pipeline"][0]["run"].endswith(
        "optimized_neurotech_ingestor.py"
    ), "❌ Modul ingestion salah!"
    print("✅ YAML pipeline valid.")


def test_ingestor_output():
    """Memastikan file JSON hasil ingesti valid dan berisi embedding."""

    print("📊 Memeriksa hasil JSON ingestion...")
    assert OUTPUT_JSON.exists(), "❌ File output JSON belum dihasilkan!"
    with open(OUTPUT_JSON) as f:
        data = json.load(f)
    assert isinstance(data, list) and len(data) > 0, "❌ JSON kosong!"
    sample = data[0]
    assert "title" in sample and "embedding" in sample, "❌ Format JSON tidak lengkap!"
    assert len(sample["embedding"]) > 100, "❌ Embedding terlalu pendek!"
    print(f"✅ Ditemukan {len(data)} unit pengetahuan, contoh judul: {sample['title']}")


def test_embedding_quality():
    """Cek konsistensi embedding semantik antar-chunk."""

    print("🧠 Menguji koherensi embedding...")
    with open(OUTPUT_JSON) as f:
        data = json.load(f)
    vectors = np.array([d["embedding"] for d in data[:5]])
    cos_sim = np.dot(vectors[0], vectors[1]) / (
        np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1])
    )
    assert 0.6 <= cos_sim <= 0.98, f"❌ Embedding tidak koheren: {cos_sim:.3f}"
    print(f"✅ Koherensi embedding reflektif stabil (cos-sim: {cos_sim:.3f})")


def test_semantic_query():
    """Simulasi query RAG sederhana untuk sanity check."""

    print("🔍 Melakukan query semantik uji...")
    query = "state-space model untuk neuroprosthesis"
    query_vec = model.encode(query)
    with open(OUTPUT_JSON) as f:
        data = json.load(f)
    scores = []
    for d in data:
        emb = np.array(d["embedding"])
        sim = np.dot(query_vec, emb) / (
            np.linalg.norm(query_vec) * np.linalg.norm(emb)
        )
        scores.append((d["title"], sim))
    top_result = sorted(scores, key=lambda x: x[1], reverse=True)[0]
    print(
        f"✅ Hasil query tertinggi: {top_result[0]} "
        f"(similaritas={top_result[1]:.3f})"
    )
    assert top_result[1] > 0.7, "❌ Hasil query tidak relevan!"


def log_results_to_journal():
    """Catat hasil pengujian ke Journal Vault."""

    journal_dir = BASE_DIR / "vaults/journal_vault"
    journal_dir.mkdir(parents=True, exist_ok=True)
    log_path = journal_dir / "test_rag_ingestor_log.json"
    log_data = {
        "status": "OK",
        "tests": ["YAML", "Ingestion", "Embedding", "Query"],
        "result": "All passed",
        "confidence": 0.95,
    }
    with open(log_path, "w") as f:
        json.dump(log_data, f, indent=2)
    print(f"🧾 Log hasil tes disimpan ke: {log_path}")


if __name__ == "__main__":
    print("\n🚀 Menjalankan pengujian integrasi RAG Neurotech TUYUL...\n")
    test_yaml_integrity()
    test_ingestor_output()
    test_embedding_quality()
    test_semantic_query()
    log_results_to_journal()
    print("\n✅ Semua pengujian selesai. Sistem RAG reflektif stabil.\n")
