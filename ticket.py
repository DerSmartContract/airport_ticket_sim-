import hashlib
from dataclasses import dataclass
from flight import Flight
from datetime import datetime

@dataclass
class Ticket:
    flight: Flight
    passenger_name: str
    booking_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket_id: str = ""

    def __post_init__(self) -> None:
        self.passenger_name = self.passenger_name.strip()
        self._validate()
        self.ticket_id = self._generate_ticket_id()

    def _validate(self) -> None:
        if not self.passenger_name:
            raise ValueError("Der Passagiername darf nicht leer sein.")
        if not isinstance(self.flight, Flight):
            raise TypeError("flight muss ein Flight-Objekt sein.")

    def _generate_ticket_id(self) -> str:
        # Mehr Attribute für bessere Einzigartigkeit
        data = f"{self.flight.flight_number}|{self.passenger_name}|{self.booking_time}".encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def __str__(self) -> str:
        return (
            f"Ticket ID: {self.ticket_id}\n"
            f"Passenger: {self.passenger_name}\n"
            f"Flight: {self.flight}\n"
            f"Booking Time: {self.booking_time}"
        )