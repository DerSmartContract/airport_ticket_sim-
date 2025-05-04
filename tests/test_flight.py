import pytest
from flight import Flight

def test_flight_creation():
    flight = Flight("LH123", "Berlin", "London", 300)
    assert flight.flight_number == "LH123"
    assert flight.price == 300

def test_flight_invalid_price():
    with pytest.raises(ValueError):
        Flight("LH123", "Berlin", "London", -50)

def test_flight_empty_origin():
    with pytest.raises(ValueError):
        Flight("LH123", "", "London", 300)