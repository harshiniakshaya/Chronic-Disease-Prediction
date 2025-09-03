# Import necessary libraries
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Create a FastAPI app instance
app = FastAPI(title="Multi-Disease Prediction API",
              description="An API to predict Chronic Kidney Disease (CKD) and Liver Disease.",
              version="2.0")

# Load the model and scaler from within the 'app' folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVED_MODELS_DIR = os.path.join(BASE_DIR, "saved_models")

# Kidney Model and Scaler
KIDNEY_MODEL_PATH = os.path.join(SAVED_MODELS_DIR, "kidney_model.joblib")
KIDNEY_SCALER_PATH = os.path.join(SAVED_MODELS_DIR, "kidney_scaler.joblib")
kidney_model = joblib.load(KIDNEY_MODEL_PATH)
kidney_scaler = joblib.load(KIDNEY_SCALER_PATH)

# Liver Model and Scaler
LIVER_MODEL_PATH = os.path.join(SAVED_MODELS_DIR, "liver_model.joblib")
LIVER_SCALER_PATH = os.path.join(SAVED_MODELS_DIR, "liver_scaler.joblib")
liver_model = joblib.load(LIVER_MODEL_PATH)
liver_scaler = joblib.load(LIVER_SCALER_PATH)

# Define the input data structure using Pydantic
class KidneyPatientData(BaseModel):
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

class LiverPatientData(BaseModel):
    Age: int
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphotase: int
    Alamine_Aminotransferase: int
    Aspartate_Aminotransferase: int
    Total_Protiens: float
    Albumin: float
    Albumin_and_Globulin_Ratio: float
    Gender_Male: int

# Health check endpoint
@app.get("/")
def read_root():
    return {"status": "ok"}



# Define the prediction endpoint
@app.post("/predict/kidney")
def predict_kidney(data: KidneyPatientData):
    input_data = pd.DataFrame([data.dict()])

    feature_order = [
        "age", "bp", "sg", "al", "su",
        "rbc", "pc", "pcc", "ba", "bgr",
        "bu", "sc", "sod", "pot", "hemo",
        "pcv", "wc", "rc", "htn", "dm",
        "cad", "appet", "pe", "ane"
    ]
    input_data = input_data[feature_order]

    scaled_data = kidney_scaler.transform(input_data)
    prediction = kidney_model.predict(scaled_data)
    probability = kidney_model.predict_proba(scaled_data)

    if prediction[0] == 1:
        result = "Chronic Kidney Disease (CKD)"
        confidence = probability[0][1]
    else:
        result = "Not Chronic Kidney Disease (Not CKD)"
        confidence = probability[0][0]

    return {
        "disease": "Kidney Disease",
        "prediction": result,
        "confidence_score": f"{confidence:.2f}"
    }

@app.post("/predict/liver")
def predict_liver(data: LiverPatientData):
    input_data = pd.DataFrame([data.model_dump()])
    feature_order = [
        "Age",
        "Total_Bilirubin",
        "Direct_Bilirubin",
        "Alkaline_Phosphotase",
        "Alamine_Aminotransferase",
        "Aspartate_Aminotransferase",
        "Total_Protiens",
        "Albumin",
        "Albumin_and_Globulin_Ratio",
        "Gender_Male"
    ]
    input_data = input_data[feature_order]

    scaled_data = liver_scaler.transform(input_data)
    prediction = liver_model.predict(scaled_data)
    probability = liver_model.predict_proba(scaled_data)

    if prediction[0] == 1:
        result = "Liver Disease Detected"
        confidence = probability[0][1]
    else:
        result = "No Liver Disease Detected"
        confidence = probability[0][0]

    return {
        "disease": "Liver Disease",
        "prediction": result,
        "confidence_score": f"{confidence:.2f}"
    }
    