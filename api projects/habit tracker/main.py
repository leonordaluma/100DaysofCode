from keys import token
from datetime import datetime
import requests


TOKEN = token
USERNAME = "stormpo0per"
ID = "mygraph"
headers = {
    "X-USER-TOKEN" : TOKEN
}

pixela_url = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# r = requests.post(url=pixela_url, json=user_parameters)
# print(r.text)

graphs_url = f"{pixela_url}/{USERNAME}/graphs"
graph_parameters = {
    "id": ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Tokyo"
}

# r = requests.post(url=graphs_url, json=graph_parameters, headers=headers)
# print(r.text)
today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel = f"{graphs_url}/{ID}"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "51"
}

# r = requests.post(url=pixel, json=pixel_parameters, headers=headers)
# print(r.text)