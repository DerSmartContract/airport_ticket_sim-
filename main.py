from flight import Flight
from ticket import Ticket
from payment import PaymentProcessor
from logger_utils import Logger
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

def search_ticket(blockchain: Blockchain) -> None:
    ticket_id = input("\nTicket-ID zum Suchen eingeben: ").strip()
    block = blockchain.get_block_by_ticket_id(ticket_id)
    if block:
        print("\nGefundener Block:")
        print(block)
    else:
        print("Kein Block mit dieser Ticket-ID gefunden.")

def main() -> None:
    print("Willkommen zur Flughafen-Ticket-Simulation\n")

    flights = list_flights()
    blockchain = Blockchain()

    # Blockchain beim Start laden
    try:
        blockchain.load_chain_from_file()
        if blockchain.is_chain_valid():
            print("\nBestehende Blockchain geladen und gültig.")
            print(f"Aktuelle Kettenlänge: {blockchain.get_chain_length()} Blöcke\n")
            Logger.log("Blockchain-Datei und Hash geprüft. Integrität OK.", level="INFO")
        else:
            print("Warnung: Blockchain ist inkonsistent!")
            Logger.log("Blockchain inkonsistent trotz gültigem Datei-Hash.", level="WARNING")
    except ValueError as e:
        Logger.log(f"Integritätsfehler beim Laden: {e}", level="ERROR")
        print(f"\n❌ Integritätsfehler: {e}")
        return

    # Flugoptionen anzeigen
    for idx, flight in enumerate(flights, start=1):
        print(f"{idx}. {flight}")

    while True:
        selected_flight = select_flight(flights)
        passenger_name = get_passenger_name()

        try:
            # HIER: currency explizit setzen (Version 2.3 Änderung)
            if PaymentProcessor.process_payment(selected_flight.price, currency="USD"):
                ticket = Ticket(selected_flight, passenger_name)
                print("\n--- Dein Ticket ---")
                print(ticket)

                Logger.log(
                    f"Buchung: {ticket.ticket_id} | "
                    f"Passagier: {passenger_name} | "
                    f"Flug: {selected_flight}",
                    level="INFO"
                )

                block = blockchain.add_ticket(ticket)
                print("\nBlock hinzugefügt:")
                print(block)

        except Exception as e:
            Logger.log(f"Fehler während der Buchung: {e}", level="ERROR")
            print(f"Fehler während der Buchung: {e}")

        another = input("\nMöchten Sie ein weiteres Ticket buchen? (ja/nein/suche): ").strip().lower()
        if another == "suche":
            search_ticket(blockchain)
            continue
        elif another != "ja":
            break

    print("\n--- Blockchain der Tickets ---")
    blockchain.display_chain()

    # Blockchain-Integrität prüfen
    if blockchain.is_chain_valid():
        print("\nBlockchain-Integrität: OK ✅")
        Logger.log("Blockchain-Integrität nach Buchung: OK.", level="INFO")
    else:
        Logger.log("Blockchain-Integrität: FEHLER ❌ Manipulation erkannt.", level="ERROR")
        print("\nBlockchain-Integrität: FEHLER ❌ Manipulation erkannt.")

    # Blockchain am Ende speichern (inkl. Hash-Datei)
    blockchain.save_chain_to_file()
    print("Blockchain und Integritätshash gespeichert.")

    print("\nVielen Dank für Ihre Buchungen. Auf Wiedersehen.")

if __name__ == "__main__":
    main()