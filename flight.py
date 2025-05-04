class Flight:
    def __init__(self, flight_number, origin, destination, price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"{self.flight_number}: {self.origin} -> {self.destination} (${self.price:.2f})"