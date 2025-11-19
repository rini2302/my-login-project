import json
import pytest
from src.backend.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    resp = client.post(
        "/api/login",
        data=json.dumps({"username": "user", "password": "pass"}),
        content_type="application/json"
    )
    assert resp.status_code == 200
    data = resp.get_json()
    assert "token" in data

def test_login_invalid_credentials(client):
    resp = client.post(
        "/api/login",
        data=json.dumps({"username": "user", "password": "wrong"}),
        content_type="application/json"
    )
    assert resp.status_code == 401
    assert resp.get_json()["message"] == "invalid credentials"

def test_login_missing_fields(client):
    resp = client.post(
        "/api/login",
        data=json.dumps({}),
        content_type="application/json"
    )
    assert resp.status_code == 400
    assert "required" in resp.get_json()["message"]
