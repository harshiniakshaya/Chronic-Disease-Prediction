import requests

url = "http://127.0.0.1:8000/predict/liver"

data = {
    "Age": 45,
    "Total_Bilirubin": 1.2,
    "Direct_Bilirubin": 0.5,
    "Alkaline_Phosphotase": 210,
    "Alamine_Aminotransferase": 35,
    "Aspartate_Aminotransferase": 40,
    "Total_Protiens": 6.5,
    "Albumin": 3.0,
    "Albumin_and_Globulin_Ratio": 1.0,
    "Gender_Male": 1   # 1 = Male, 0 = Female
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)  
