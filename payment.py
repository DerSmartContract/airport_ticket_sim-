from logger_utils import Logger

class PaymentProcessor:
    SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP"]  # Vorbereitet für später

    @staticmethod
    def process_payment(amount: float, currency: str = "USD") -> bool:
        """
        Simuliert die Verarbeitung einer Zahlung.

        :param amount: Zahlungsbetrag
        :param currency: Währung (derzeit nur zu Demonstrationszwecken)
        :return: True, wenn Zahlung erfolgreich
        """
        PaymentProcessor._validate_amount(amount)
        PaymentProcessor._validate_currency(currency)

        try:
            print(f"Zahlung von {amount:.2f} {currency} erfolgreich verarbeitet.")
            Logger.log(
                f"Zahlung verarbeitet: {amount:.2f} {currency}",
                level="INFO"
            )
            return True
        except Exception as e:
            Logger.log(
                f"Zahlungsfehler: {e}",
                level="ERROR"
            )
            print(f"Zahlungsfehler: {e}")
            return False

    @staticmethod
    def _validate_amount(amount: float) -> None:
        if amount <= 0:
            raise ValueError("Der Zahlungsbetrag muss größer als 0 sein.")

    @staticmethod
    def _validate_currency(currency: str) -> None:
        if currency not in PaymentProcessor.SUPPORTED_CURRENCIES:
            raise ValueError(f"Währung {currency} wird nicht unterstützt.")