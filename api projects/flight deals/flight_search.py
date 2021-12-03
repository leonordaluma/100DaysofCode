from flight_data import FlightData
from pprint import pprint
import requests
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

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PHP" 
        }
        
        r = requests.get(url=f"{ENDPOINT}/v2/search", headers=headers, params=parameters)
        raw_data = r.json()
        #     data = raw_data[0]
        #     flight_data = FlightData(
        #         price=data["price"],
        #         origin_city=data["route"][0]["cityFrom"],
        #         origin_airport=data["route"][0]["flyFrom"],
        #         destination_city=data["route"][0]["cityTo"],
        #         destination_airport=data["route"][0]["flyTo"],
        #         out_date=data["route"][0]["local_departure"].split("T")[0],
        #         return_date=data["route"][1]["local_departure"].split("T")[0]
        #     )
        #     print(f"{flight_data.destination_city}: P{flight_data.price}")
        #     return flight_data
        # else:
        #     return None
        pprint(raw_data)