from api_key import API_KEY, account_sid, auth_token
import requests
from twilio.rest import Client

LAT = 8.001110
LONG = 124.284821

parameters = {
    "lat" : LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data["hourly"][:12]


will_rain = False
for hour_data in weather_data:
    condition = hour_data["weather"][0]["id"]
    if int(condition) > 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
else:
    print("You're good to go.")
        