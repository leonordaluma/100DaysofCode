from requests.api import head
from keys import api_key
import requests


ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = api_key


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{ENDPOINT}/locations/query"
        header = {
            "apikey": API_KEY
        }
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        r = requests.get(url=location_endpoint,
                         params=parameters, headers=header)
        results = r.json()["locations"]
        code = results[0]["code"]
        return code
