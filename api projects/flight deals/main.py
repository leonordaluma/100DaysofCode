from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

for row in sheet_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_destination_code(row["city"])
        data_manager.update_destination_data(iata=iata_code, id=row["id"])
        
    

print(data_manager.destination_data)