from api_key import API_KEY
import requests

LAT = 14.599512
LONG = 120.984222

parameters = {
    "lat" : LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
forty_eight_hours = data["hourly"][47]
print(data)