from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import os

app = FastAPI(
    title="Insurance Prediction API"
)

# ----------------------
# Load Models
# ----------------------

with open("insurance_premium.pkl", "rb") as f:
    premium_model = pickle.load(f)

with open("score.pkl", "rb") as f:
    score_model = pickle.load(f)

with open("risk.pkl", "rb") as f:
    risk_model = pickle.load(f)





# ----------------------
# Request Schema
# ----------------------

class InsuranceRequest(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str


# ----------------------
# Feature Engineering
# ----------------------

def bmi_category(bmi):

    if bmi < 18.5:
        return "underweight"

    elif bmi < 25:
        return "normal"

    elif bmi < 30:
        return "overweight"

    return "obese"


def smoking_risk(smoker, bmi):

    if smoker == "yes" and bmi > 30:
        return "high"

    elif smoker == "yes" or bmi > 27:
        return "medium"

    return "low"


# ----------------------
# Routes
# ----------------------

@app.get("/")
def home():
    return {
        "message": "Insurance Prediction API Running"
    }


@app.post("/predict")
def predict(data: InsuranceRequest):

    bmi_cat = bmi_category(data.bmi)

    smoke_risk = smoking_risk(
        data.smoker,
        data.bmi
    )

    input_df = pd.DataFrame([
        {
            "age": data.age,
            "sex": data.sex,
            "children": data.children,
            "region": data.region,
            "bmi_category": bmi_cat,
            "smoking_risk": smoke_risk
        }
    ])

    premium = premium_model.predict(input_df)[0]

    risk_score = score_model.predict(input_df)[0]

    risk = risk_model.predict(input_df)[0]


   
        
    return {
    "predicted_premium": float(premium),
    "risk_score": float(risk_score),
    "health_risk": str(risk)
}