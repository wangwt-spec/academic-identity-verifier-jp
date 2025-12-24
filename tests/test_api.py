from fastapi.testclient import TestClient
from identity_verifier.api import app

client = TestClient(app)

def test_verify_endpoint_non_adjudicative():
    response = client.post(
        "/verify",
        json={
            "name": "Test Person",
            "affiliation": "Test Institute",
            "sources": []
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "evidence_level" in data
    assert "Human review required" in data["description"]


