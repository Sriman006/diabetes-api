from fastapi.testclient import TestClient
import httpx
from demo import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict", json={
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 79,
        "BMI": 24.2,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 30
    })
    assert response.status_code == 200
    assert "diabetes_risk" in response.json()
    
if __name__ == "__main__":
    test_predict()
    print("Test passed ✅")