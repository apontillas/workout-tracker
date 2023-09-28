import requests
from datetime import datetime
import os

NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_ENDPOINT = os.environ["NUTRITIONIX_ENDPOINT"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

today = datetime.now()

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}


params = {
    "query": input("What exercises did you do? "),
}

res_exercise = requests.post(url=NUTRITIONIX_ENDPOINT, data=params, headers=headers)
data = res_exercise.json()["exercises"]

date = today.strftime("%y/%m/%d")
time = today.strftime("%X")

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for workout in data:
    body = {"workout": {
        "date": date,
        "time": time,
        "exercise": workout['name'].title(),
        "duration": workout["duration_min"],
        "calories": workout["nf_calories"]
        }
    }

    res_sheet = requests.post(url=SHEETY_ENDPOINT, json=body, headers=headers)
    print(res_sheet.status_code)



