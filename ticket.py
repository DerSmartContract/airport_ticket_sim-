import hashlib

class Ticket:
    def __init__(self, flight, passenger_name):
        self.flight = flight
        self.passenger_name = passenger_name
        self.ticket_id = self._generate_ticket_id()

    def _generate_ticket_id(self):
        data = f"{self.flight.flight_number}{self.passenger_name}".encode()
        return hashlib.sha256(data).hexdigest()

    def __str__(self):
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Passenger: {self.passenger_name}\n"
                f"Flight: {self.flight}")