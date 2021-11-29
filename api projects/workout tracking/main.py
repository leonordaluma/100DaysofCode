from keys import app_id, api_key
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
parameters = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

r = requests.post(url=nutritionix_endpoint, json=parameters, headers=HEADERS)
result = r.json()
print(result)