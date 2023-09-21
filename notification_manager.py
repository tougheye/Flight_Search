from twilio.rest import Client
from flight_data import FlightData

t_sid = ENTER_YOUR_OWN_SID
t_token = ENTER_YOUR_OWN_TOKEN


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid=t_sid, password=t_token)

    def print_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+12566023852", to="+12027483913")
        print(message.sid)
