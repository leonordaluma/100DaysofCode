import requests

SHEETY_ENDPOINT = "https://api.sheety.co/af73963297d466e6b7310d8445045a09/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        r = requests.get(url=SHEETY_ENDPOINT)
        data = r.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_data(self, iata,id):
        new_data = {
            "price": {
                "iataCode": iata
            }
        }
            
        r = requests.put(url=f"{SHEETY_ENDPOINT}/{id}", json=new_data)
        print(r.text)