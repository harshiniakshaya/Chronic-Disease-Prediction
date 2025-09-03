import requests

url = "http://127.0.0.1:8000/predict/heart"

data = {
    "age": 52,
    "sex": 1,             # 1 = Male, 0 = Female
    "cp": 2,              # Chest pain type (0-3)
    "trestbps": 130,      # Resting blood pressure (mm Hg)
    "chol": 250,          # Serum cholesterol (mg/dl)
    "fbs": 0,             # Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
    "restecg": 1,         # Resting ECG results (0-2)
    "thalach": 170,       # Maximum heart rate achieved
    "exang": 0,           # Exercise induced angina (1 = Yes, 0 = No)
    "oldpeak": 1.5,       # ST depression induced by exercise
    "slope": 2,           # Slope of ST segment (0-2)
    "ca": 0,              # Number of major vessels (0-3)
    "thal": 2             # Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
