import requests
from pprint import pprint
from flight_data import FlightData
from datetime import datetime, timedelta

sheety_get_ep = "https://api.sheety.co/ee8068b4fb3e9f07d984cd0fd0d204ab/flightDeals/flightDeals"
sheety_get_req = requests.get(sheety_get_ep)
sheety_data = sheety_get_req.json()['flightDeals']


tomorrow_date = datetime.now()
tomorrow_str = tomorrow_date.strftime("%d/%m/%Y")
six_months = tomorrow_date + timedelta(days=180)
six_months_str = six_months.strftime("%d/%m/%Y")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_ep = 'https://api.tequila.kiwi.com/'
        self.tequila_api_key = ADD_YOUR_OWN_API_KEY
        self.call_api = "https://api.tequila.kiwi.com/v2/search"

    def fetch_iata(self, city_data):
        # this function will return the IATA names from kiwi data for the cities in Sheet data
        iata_dict = {}
        for city in city_data:
            header = {'apikey': tequila_api_key}
            query = {'term': city,
                     'location_types': 'city',
                     'limit': 20}
            teq_request = requests.get(url=f"{tequila_ep}locations/query",
                                       headers=header, params=query)
            # print(teq_request.status_code)
            iata_dict[teq_request.json()['locations'][0]['name']] = teq_request.json()['locations'][0]['code']

        return iata_dict

    def fetch_flight(self, from_city, to_city, curr):
        header = {'apikey': self.tequila_api_key}
        parameters = {'fly_from': from_city,
                      'fly_to': to_city,
                      'date_from': tomorrow_str,
                      'date_to': six_months_str,
                      'curr': curr,
                      }
        search_get = requests.get(url=self.call_api, headers=header, params=parameters)
        print(search_get.status_code)
        search_data = search_get.json()['data'][0]
        print(f"{search_data['cityTo']} - {search_data['price']}")
        f_data = FlightData(
            dept_date=search_data['local_departure'].split('T')[0],
            return_date=search_data['route'][0]['local_arrival'].split('T')[0],
            dept_city=search_data['cityFrom'],
            dest_city=search_data['cityTo'],
            dept_apt=search_data['flyFrom'],
            dest_apt=search_data['flyTo'],
            price=search_data['price'])

        return f_data
