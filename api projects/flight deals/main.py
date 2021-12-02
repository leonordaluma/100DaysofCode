from data_manager import DataManager
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)