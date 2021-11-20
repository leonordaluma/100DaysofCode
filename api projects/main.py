import requests
from datetime import *

from requests.api import request

LAT = 23.697809
LONG = 120.960518

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_long = float(data["iss_position"]["longitude"])

# Your position is +5 or -5 degrees of the ISS position 

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
now = datetime.now()


print(data["results"]["sunrise"])
print(data["results"]["sunset"])
print(now)


# if the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up 
# BONUS: run code every 60 seconds 