import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from main import app

client = TestClient(app)

@pytest.fixture
def mock_redis():
    with patch("main.r") as mock:
        yield mock

def test_create_job(mock_redis):
    # Setup mock for pipeline
    pipeline_mock = MagicMock()
    mock_redis.pipeline.return_value = pipeline_mock

    response = client.post("/jobs")
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data
    
    # Check that pipeline was used correctly
    pipeline_mock.lpush.assert_called_once_with("job", data["job_id"])
    pipeline_mock.hset.assert_called_once_with(f"job:{data['job_id']}", "status", "queued")
    pipeline_mock.execute.assert_called_once()

def test_get_job_exists(mock_redis):
    mock_redis.hget.return_value = b"queued"
    
    response = client.get("/jobs/test-id-123")
    assert response.status_code == 200
    data = response.json()
    assert data["job_id"] == "test-id-123"
    assert data["status"] == "queued"
    mock_redis.hget.assert_called_once_with("job:test-id-123", "status")

def test_get_job_not_found(mock_redis):
    mock_redis.hget.return_value = None
    
    response = client.get("/jobs/nonexistent-id")
    assert response.status_code == 200
    assert response.json() == {"error": "not found"}
