from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, time, timedelta
from pprint import pprint
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

ORIGIN_CITY_IATA = "LON"
data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_destination_code(row["city"])
        data_manager.update_destination_data(iata=iata_code, id=row["id"])


tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(30 * 6))

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

# pprint(flight)
