## payment.py ##
class PaymentProcessor:
    @staticmethod
    def process_payment(amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Der Zahlungsbetrag muss größer als 0 sein.")
        try:
            print(f"Zahlung von ${amount:.2f} erfolgreich verarbeitet.")
            return True
        except Exception as e:
            print(f"Zahlungsfehler: {e}")
            return False