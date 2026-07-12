from fastapi.testclient import TestClient

from water_quality.api import app


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction_requires_a_loaded_model():
    payload = {
        "ph": 7.0, "Hardness": 180, "Solids": 20000,
        "Chloramines": 7, "Sulfate": 330, "Conductivity": 420,
        "Organic_carbon": 14, "Trihalomethanes": 65, "Turbidity": 4,
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
    assert response.status_code == 503
