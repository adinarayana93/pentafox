from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees", json={
        "name": "John",
        "address": "Delhi",
        "salary": 50000,
        "age": 25
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John"
