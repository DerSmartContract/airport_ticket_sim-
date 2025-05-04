from flight import Flight
from ticket import Ticket
from payment import PaymentProcessor
from logger import Logger
from blockchain_manager import Blockchain
from typing import List

def list_flights() -> List[Flight]:
    return [
        Flight("AB123", "Berlin", "New York", 500),
        Flight("CD456", "Paris", "Tokyo", 750),
        Flight("EF789", "London", "Toronto", 400)
    ]

def select_flight(flights: List[Flight]) -> Flight:
    while True:
        try:
            choice = int(input("Bitte wählen Sie einen Flug (Nummer): ").strip()) - 1
            if 0 <= choice < len(flights):
                return flights[choice]
            else:
                print(f"Bitte geben Sie eine Zahl zwischen 1 und {len(flights)} ein.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")

def get_passenger_name() -> str:
    while True:
        name = input("Name des Passagiers: ").strip()
        if name:
            return name
        print("Der Name darf nicht leer sein.")

def main() -> None:
    print("Willkommen zur Flughafen-Ticket-Simulation\n")

    flights = list_flights()
    blockchain = Blockchain()

    # Blockchain beim Start laden
    blockchain.load_chain_from_file()

    # Blockchain-Integrität prüfen
    if not blockchain.is_chain_valid():
        print("\nWarnung: Die bestehende Blockchain ist ungültig!")
    else:
        print("\nBestehende Blockchain geladen und gültig.")

    # Flugoptionen anzeigen
    for idx, flight in enumerate(flights, start=1):
        print(f"{idx}. {flight}")

    while True:
        selected_flight = select_flight(flights)
        passenger_name = get_passenger_name()

        try:
            if PaymentProcessor.process_payment(selected_flight.price):
                ticket = Ticket(selected_flight, passenger_name)
                print("\n--- Dein Ticket ---")
                print(ticket)

                Logger.log(
                    f"Buchung: {ticket.ticket_id} | "
                    f"Passagier: {passenger_name} | "
                    f"Flug: {selected_flight}"
                )

                block = blockchain.add_ticket(ticket)
                print("\nBlock hinzugefügt:")
                print(block)

        except Exception as e:
            print(f"Fehler während der Buchung: {e}")

        another = input("\nMöchten Sie ein weiteres Ticket buchen? (ja/nein): ").strip().lower()
        if another != "ja":
            break

    print("\n--- Blockchain der Tickets ---")
    blockchain.display_chain()

    # Blockchain-Integrität prüfen
    if blockchain.is_chain_valid():
        print("\nBlockchain-Integrität: OK ✅")
    else:
        print("\nBlockchain-Integrität: FEHLER ❌ Manipulation erkannt.")

    # Blockchain am Ende speichern
    blockchain.save_chain_to_file()

    print("\nVielen Dank für Ihre Buchungen. Auf Wiedersehen.")

if __name__ == "__main__":
    main()