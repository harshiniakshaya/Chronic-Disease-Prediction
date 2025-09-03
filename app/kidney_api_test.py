import requests

url = "http://127.0.0.1:8000/predict/kidney"

data = {
    "age": 50,
    "bp": 80,
    "sg": 1.02,
    "al": 1,
    "su": 0,
    "rbc": 1,
    "pc": 1,
    "pcc": 0,
    "ba": 0,
    "bgr": 150,
    "bu": 40,
    "sc": 1.2,
    "sod": 135,
    "pot": 4.5,
    "hemo": 15.5,
    "pcv": 45,
    "wc": 8000,
    "rc": 5.2,
    "htn": 1,
    "dm": 0,
    "cad": 0,
    "appet": 1,
    "pe": 0,
    "ane": 0
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)  # print raw response
