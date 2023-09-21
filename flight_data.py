class FlightData:
    def __init__(self, dept_city, dept_apt, dest_city, dest_apt, price, dept_date, return_date):
        self.from_city = dept_city,
        self.from_iata = dept_apt,
        self.to_city = dest_city,
        self.to_iata = dest_apt,
        self.price = price,
        self.from_date = dept_date,
        self.return_date = return_date

