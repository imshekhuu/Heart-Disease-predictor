from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pandas as pd
import joblib
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "KNN_heart.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

class UserInput(BaseModel):
    Age: int
    sex: Literal["Male", "Female"]
    ChestPainType: Literal["ATA", "NAP", "TA", "ASY"]
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: Literal["Normal", "ST", "LVH"]
    MaxHR: int
    ExerciseAngina: Literal["Y", "N"]
    Oldpeak: float
    st_slope: Literal["Up", "Flat", "Down"]

@app.post("/predict")
def predict(data: UserInput):

    raw = {
        "Age": data.Age,
        "RestingBP": data.RestingBP,
        "Cholesterol": data.Cholesterol,
        "FastingBS": data.FastingBS,
        "MaxHR": data.MaxHR,
        "Oldpeak": data.Oldpeak,
        "Sex_" + data.sex: 1,
        "ChestPainType_" + data.ChestPainType: 1,
        "RestingECG_" + data.RestingECG: 1,
        "ExerciseAngina_" + data.ExerciseAngina: 1,
        "ST_Slope_" + data.st_slope: 1
    }

    df = pd.DataFrame([raw])

    for col in columns:
        if col not in df.columns:
            df[col] = 0

    df = df[columns]
    scaled = scaler.transform(df)
    pred = int(model.predict(scaled)[0])

    return {"prediction": pred}
