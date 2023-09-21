#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_search
from pprint import pprint
from notification_manager import NotificationManager

#getting data from google
sheet_data = flight_search.sheety_data
# print(type(sheet_data[0]['lowestPrice']))

cities = [i['city'] for i in sheet_data]    #isolate the cities from the sheet data
# print(cities)

f_search = flight_search.FlightSearch()
iatas = f_search.fetch_iata(cities)         #search IATA codes for cities

for item in sheet_data:
    item['iataCode'] = iatas[item['city']]

data_sheet = DataManager(sheet_data)
data_sheet.update_iata()

for dest in sheet_data:
    flight_details = f_search.fetch_flight(from_city="LON", to_city=dest['iataCode'], curr="GBP")
    if flight_details.price < dest.get("lowestPrice"):          #also tried dest["lowestPrice"]
        texter = NotificationManager()
        texter.print_message(
            message=f"Low price alert! Only 💷{flight_details.price} to fly from"
                    f"{flight_details.from_city}-{flight_details.from_iata}"
                    f"to {flight_details.to_city}-{flight_details.to_iata},"
                    f"from {flight_details.from_date} to {flight_details.return_date}.")
