class PaymentProcessor:
    @staticmethod
    def process_payment(amount):
        print(f"Zahlung von ${amount:.2f} erfolgreich verarbeitet.")
        return True