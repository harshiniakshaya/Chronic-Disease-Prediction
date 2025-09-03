# Import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Create a FastAPI app instance
app = FastAPI(title="Kidney Disease Prediction API")

# Load the model and scaler from within the 'app' folder
model = joblib.load('../saved_models/kidney_model.joblib')
scaler = joblib.load('../saved_models/kidney_scaler.joblib')

# Define the input data structure using Pydantic
class PatientData(BaseModel):
    age: float
    bp: float
    sg: float
    al: float
    su: float
    rbc: int
    pc: int
    pcc: int
    ba: int
    bgr: float
    bu: float
    sc: float
    sod: float
    pot: float
    hemo: float
    pcv: float
    wc: float
    rc: float
    htn: int
    dm: int
    cad: int
    appet: int
    pe: int
    ane: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: PatientData):
    input_data = pd.DataFrame([data.dict()])
    
    # This is crucial: Ensure the column order is the same as the training data
    feature_order = [
        "age", "bp", "sg", "al", "su",
        "rbc", "pc", "pcc", "ba", "bgr",
        "bu", "sc", "sod", "pot", "hemo",
        "pcv", "wc", "rc", "htn", "dm",
        "cad", "appet", "pe", "ane"
    ]
    input_data = input_data[feature_order]

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    probability = model.predict_proba(scaled_data)

    if prediction[0] == 1:
        result = "Chronic Kidney Disease (CKD)"
        confidence = probability[0][1]
    else:
        result = "Not Chronic Kidney Disease (Not CKD)"
        confidence = probability[0][0]

    return {
        "prediction": result,
        "confidence_score": f"{confidence:.2f}"
    }

# Health check endpoint
@app.get("/")
def read_root():
    return {"status": "ok"}