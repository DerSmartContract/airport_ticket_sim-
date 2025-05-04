import pytest
from payment import PaymentProcessor

def test_valid_payment():
    assert PaymentProcessor.process_payment(100) is True

def test_invalid_payment():
    with pytest.raises(ValueError):
        PaymentProcessor.process_payment(-10)