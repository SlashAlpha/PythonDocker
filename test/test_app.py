import pytest
from pathlib import Path
from src.app import app


@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve()
    app.config["TESTING"] = True
    yield app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

