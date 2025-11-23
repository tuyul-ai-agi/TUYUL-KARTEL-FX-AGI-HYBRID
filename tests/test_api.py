"""Basic API tests for TUYUL-FX-HYBRID."""

import pytest
from fastapi.testclient import TestClient
import os
import sys

# Set minimal environment variables for testing
os.environ["OPENAI_API_KEY"] = "test-key"
os.environ["GITHUB_TOKEN"] = "test-token"
os.environ["GITHUB_KNOWLEDGE_VAULT_REPO"] = "test/knowledge"
os.environ["GITHUB_JOURNAL_VAULT_REPO"] = "test/journal"
os.environ["SECRET_KEY"] = "test-secret-key-for-testing-only"

from src.tuyul_fx_hybrid.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "TUYUL-FX-HYBRID" in data["data"]["name"]


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "v5.4.0"


def test_version():
    """Test version endpoint."""
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert data["version"] == "v5.4.0"
    assert data["name"] == "TUYUL-FX-HYBRID"


def test_system_status():
    """Test system status endpoint."""
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "fusion" in data["data"]
    assert "reflex" in data["data"]
    assert "risk" in data["data"]


def test_fusion_register_source():
    """Test registering a data source."""
    response = client.post(
        "/fusion/register-source",
        json={
            "source_id": "test_source",
            "source_type": "api",
            "metadata": {"test": "data"}
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_reflex_add_rule():
    """Test adding a reflex rule."""
    response = client.post(
        "/reflex/add-rule",
        json={
            "name": "test_rule",
            "conditions": {"status": "active"},
            "action": "proceed",
            "confidence": 0.9
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_risk_assess():
    """Test risk assessment."""
    response = client.post(
        "/risk/assess",
        json={
            "action": {
                "id": "test_action",
                "cost": 100,
                "complexity": 0.5
            },
            "context": {
                "budget": 1000
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "risk_level" in data["data"]


def test_reflex_decide():
    """Test decision making."""
    response = client.post(
        "/reflex/decide",
        json={
            "context": {"status": "ready"},
            "options": [
                {"id": "option1", "priority": 0.8},
                {"id": "option2", "priority": 0.6}
            ],
            "mode": "fast"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "action" in data["data"]


def test_fusion_fuse():
    """Test data fusion."""
    response = client.post(
        "/fusion/fuse",
        json={
            "data_streams": [
                {
                    "source_id": "source1",
                    "data": {"value": 100},
                    "confidence": 0.9
                },
                {
                    "source_id": "source2",
                    "data": {"value": 110},
                    "confidence": 0.8
                }
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_learning_experience():
    """Test logging learning experience."""
    response = client.post(
        "/learning/experience",
        json={
            "state": {"position": "ready"},
            "action": {"type": "move"},
            "reward": 0.8
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_learning_predict_reward():
    """Test reward prediction."""
    response = client.post(
        "/learning/predict-reward",
        json={
            "state": {"position": "ready"},
            "action": {"type": "move"}
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "expected_reward" in data["data"]


def test_reflection_reflect():
    """Test reflection on decision."""
    response = client.post(
        "/reflection/reflect",
        json={
            "decision": {
                "id": "dec1",
                "action": "test_action",
                "reasoning": "test reasoning",
                "confidence": 0.8
            },
            "outcome": {
                "success": True,
                "result": "completed"
            },
            "context": {
                "environment": "test"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True


def test_config():
    """Test config endpoint."""
    response = client.get("/config")
    assert response.status_code == 200
    data = response.json()
    assert "api_version" in data
    assert "gpt_model" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
