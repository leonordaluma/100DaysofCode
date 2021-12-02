from requests.api import request
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/af73963297d466e6b7310d8445045a09/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        r = request.get(url=SHEETY_ENDPOINT)
        data = r.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data