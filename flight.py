## flight.py ##
from dataclasses import dataclass

@dataclass(frozen=True)
class Flight:
    flight_number: str
    origin: str
    destination: str
    price: float

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Der Flugpreis muss größer als 0 sein.")
        if not self.flight_number or not self.origin or not self.destination:
            raise ValueError("Flugnummer, Abflug- und Zielort dürfen nicht leer sein.")

    def __str__(self) -> str:
        return f"{self.flight_number}: {self.origin} -> {self.destination} (${self.price:.2f})"