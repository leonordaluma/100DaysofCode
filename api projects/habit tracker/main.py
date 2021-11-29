from keys import token
import requests


TOKEN = token
USERNAME = "stormpo0per"

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
    "id": "mygraph",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Tokyo"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

