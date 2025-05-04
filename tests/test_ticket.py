import pytest
from ticket import Ticket
from flight import Flight

def test_ticket_creation():
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket = Ticket(flight, "Max Mustermann")
    assert ticket.passenger_name == "Max Mustermann"
    assert len(ticket.ticket_id) == 64  # SHA-256 Länge

def test_ticket_empty_passenger():
    flight = Flight("LH123", "Berlin", "London", 300)
    with pytest.raises(ValueError):
        Ticket(flight, "")