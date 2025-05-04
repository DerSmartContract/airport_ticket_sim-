## ticket.py ##
import hashlib
from flight import Flight

class Ticket:
    def __init__(self, flight: Flight, passenger_name: str) -> None:
        if not passenger_name.strip():
            raise ValueError("Der Passagiername darf nicht leer sein.")

        self.flight = flight
        self.passenger_name = passenger_name.strip()
        self.ticket_id = self._generate_ticket_id()

    def _generate_ticket_id(self) -> str:
        # Für Sicherheit & Klarheit: delimiter "|"
        data = f"{self.flight.flight_number}|{self.passenger_name}".encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def __str__(self) -> str:
        return (
            f"Ticket ID: {self.ticket_id}\n"
            f"Passenger: {self.passenger_name}\n"
            f"Flight: {self.flight}"
        )