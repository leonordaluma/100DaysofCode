from keys import token
import requests


pixela_url = "https://pixe.la/v1/users"
user_parameters = {
    "token": token,
    "username": "stormpo0per",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

r = requests.post(url=pixela_url, json=user_parameters)
print(r.text)
