import requests
from datetime import *

LAT = 14.599512
LONG = 120.984222

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
now = datetime.now()
print(sunrise)
print(now)