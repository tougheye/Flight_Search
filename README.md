# Flight_Search

This project builds an API based app to search flight data in kiwi.com using their 
open source API portal https://api.tequila.kiwi.com. 

The DataManager class requests data saved in the google sheets through sheety api service 
that includes the names of the cities (both flights from and flights to), and desired price ranges and use them to 
request flight price data from kiwi.com

The FlighSearch class takes in the data from the sheety api and performs the following:
  1. fetch_iata() - takes the city names and searches the IATA codes for those cities 
  2. fetch_flight - takes in the origin and destination cities and the currency information.
                     It then searches the cheapest flights between those cities for the given dates.
                     It then saves the output data in the FlightData class.

     FlightData class saves the flight prices and destination data in a standardized way.

     NotificationManager class uses twilio's RESTapi Client class to send text message when the FlightSearch
     class finds a flight between the destinations for the target date ranges that are below the desired
     price range.
     
