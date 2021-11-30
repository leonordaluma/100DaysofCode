from keys import app_id, api_key
from datetime import datetime
import requests


GENDER = "female"
WEIGHT =  45
HEIGHT = 149
AGE = 22
APP_ID = app_id
API_KEY = api_key
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
input_text = input("Tell me which exercise you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/af73963297d466e6b7310d8445045a09/workoutTracking/workouts"

parameters = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

r = requests.post(url=nutritionix_endpoint, json=parameters, headers=HEADERS)
result = r.json()
exercises = result["exercises"]
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
for exercise in exercises:
    sheety_parameters = {
        "workout" : {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
res = requests.post(url=sheety_endpoint, json=sheety_parameters)
print(res.text)