import requests
from flight_data import FlightData


sheety_put_ep = "https://api.sheety.co/ee8068b4fb3e9f07d984cd0fd0d204ab/flightDeals/flightDeals/"


class DataManager:
    def __init__(self, sheet_data):
        self.data_list = sheet_data
        self.call_api = "https://api.tequila.kiwi.com/v2/search"
        self.api_key = ADD_YOUR_OWN_SHEETY_API_KEY


    def update_iata(self):
        for row in self.data_list:
            url = f"{sheety_put_ep}{row['id']}"
            put_body = {'flightDeal': {'iataCode': row['iataCode']}}
            sheety_put = requests.put(url=url, json=put_body)
            print(sheety_put.text)



