# test_api.py
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_heart():
    url = f"{BASE_URL}/predict/heart"
    data = {
        "age": 52,         # Age in years
        "sex": 1,          # 1 = Male, 0 = Female
        "cp": 2,           # Chest pain type (0-3)
        "trestbps": 130,   # Resting blood pressure (mm Hg)
        "chol": 250,       # Serum cholesterol (mg/dl)
        "fbs": 0,          # Fasting blood sugar >120 mg/dl (1 = true, 0 = false)
        "restecg": 1,      # Resting ECG results (0-2)
        "thalach": 170,    # Maximum heart rate achieved
        "exang": 0,        # Exercise induced angina (1 = yes, 0 = no)
        "oldpeak": 1.5,    # ST depression induced by exercise
        "slope": 2,        # Slope of ST segment (0-2)
        "ca": 0,           # Number of major vessels (0-3)
        "thal": 2          # Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)
    }
    response = requests.post(url, json=data)
    print("Heart Test →", response.status_code, response.json())

def test_kidney():
    url = f"{BASE_URL}/predict/kidney"
    data = {
        "age": 50,         # Age in years
        "bp": 80,          # Blood pressure
        "sg": 1.02,        # Specific gravity of urine
        "al": 1,           # Albumin in urine
        "su": 0,           # Sugar in urine
        "rbc": 1,          # Red blood cells (1 = normal, 0 = abnormal)
        "pc": 1,           # Pus cells (1 = normal, 0 = abnormal)
        "pcc": 0,          # Pus cell clumps (1 = present, 0 = absent)
        "ba": 0,           # Bacteria (1 = present, 0 = absent)
        "bgr": 150,        # Blood glucose random
        "bu": 40,          # Blood urea
        "sc": 1.2,         # Serum creatinine
        "sod": 135,        # Sodium
        "pot": 4.5,        # Potassium
        "hemo": 15.5,      # Hemoglobin
        "pcv": 45,         # Packed cell volume
        "wc": 8000,        # White blood cell count
        "rc": 5.2,         # Red blood cell count
        "htn": 1,          # Hypertension (1 = yes, 0 = no)
        "dm": 0,           # Diabetes mellitus (1 = yes, 0 = no)
        "cad": 0,          # Coronary artery disease (1 = yes, 0 = no)
        "appet": 1,        # Appetite (1 = good, 0 = poor)
        "pe": 0,           # Pedal edema (1 = yes, 0 = no)
        "ane": 0           # Anemia (1 = yes, 0 = no)
    }
    response = requests.post(url, json=data)
    print("Kidney Test →", response.status_code, response.json())

def test_liver():
    url = f"{BASE_URL}/predict/liver"
    data = {
        "Age": 45,                               # Age in years
        "Total_Bilirubin": 1.2,                  # Total bilirubin
        "Direct_Bilirubin": 0.5,                 # Direct bilirubin
        "Alkaline_Phosphotase": 210,             # Alkaline phosphotase
        "Alamine_Aminotransferase": 35,          # ALT enzyme
        "Aspartate_Aminotransferase": 40,        # AST enzyme
        "Total_Protiens": 6.5,                   # Total proteins
        "Albumin": 3.0,                          # Albumin
        "Albumin_and_Globulin_Ratio": 1.0,       # A/G ratio
        "Gender_Male": 1                          # 1 = Male, 0 = Female
    }
    response = requests.post(url, json=data)
    print("Liver Test →", response.status_code, response.json())

def test_risk():
    url = f"{BASE_URL}/predict/risk"
    data = {
        "age": 25,                               # Age in years
        "bmi": 22.5,                             # Body Mass Index
        "servings_veg_fruit_daily": 3,           # Number of servings of veggies/fruits per day
        "servings_processed_food_weekly": 2,     # Number of processed food servings per week
        "hours_exercise_weekly": 5,              # Exercise hours per week
        "hours_sleep_daily": 7.5,                # Average sleep hours per day
        "alcohol_units_weekly": 1,               # Alcohol units consumed per week
        "is_smoker": 0                            # Smoking status (0 = No, 1 = Yes)
    }
    response = requests.post(url, json=data)
    print("Lifestyle Risk Test →", response.status_code, response.json())

if __name__ == "__main__":
    test_heart()
    test_kidney()
    test_liver()
    test_risk()
