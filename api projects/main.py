import requests
from datetime import *
import smtplib
import time

LAT = 23.697809
LONG = 120.960518

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    
    if LAT - 5 <= iss_lat <= LAT + 5 and LONG-5 <= iss_long <= LONG+5:
        return True

def is_night():
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
    time = now.hour
    
    if time >= sunset or time <= sunrise:
        return True

my_email = ""
my_pd = ""

while True:
    time.sleep(60)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_pd)
    if is_iss_overhead() and is_night():
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:ISS Notifier\n\nLook up to the sky!")
 


# if the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up 
# BONUS: run code every 60 seconds 