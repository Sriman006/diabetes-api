from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


app = FastAPI()

model = joblib.load("diabetes_model.pkl")

class PatientData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
def predict(data: PatientData):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                            data.SkinThickness, data.Insulin, data.BMI,
                            data.DiabetesPedigreeFunction, data.Age]])
    prediction = model.predict(input_data)[0]
    return {"diabetes_risk": bool(prediction)}