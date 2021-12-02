from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
for data in sheet_data["city"]:
    f_data = flight_search.get_destination_code("Paris")

pprint(sheet_data)