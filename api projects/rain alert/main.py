from api_key import API_KEY
import requests

LAT = 14.599512
LONG = 120.984222

parameters = {
    "lat" : LAT,
    "long": LONG,
    "appid": API_KEY,
    
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data["current"])