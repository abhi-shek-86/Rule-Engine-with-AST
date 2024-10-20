# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_rule():
    response = client.post("/create_rule", json={"rule_string": "age > 30"})
    assert response.status_code == 200
    assert response.json()["message"] == "Rule created"

def test_combine_rules():
    response = client.post("/combine_rules", json=["age > 30", "salary > 50000"])
    assert response.status_code == 200
    assert response.json()["message"] == "Rules combined"

def test_evaluate_rule():
    response = client.post("/evaluate_rule", json={"data": {"age": 35, "salary": 60000}})
    assert response.status_code == 200
    assert response.json()["result"] == True
