from flight import Flight
from ticket import Ticket
from payment import PaymentProcessor
from logger import Logger
from blockchain_manager import Blockchain

def list_flights():
    return [
        Flight("AB123", "Berlin", "New York", 500),
        Flight("CD456", "Paris", "Tokyo", 750),
        Flight("EF789", "London", "Toronto", 400)
    ]

def select_flight(flights):
    while True:
        try:
            choice = int(input("Wähle deinen Flug (Nummer): ")) - 1
            if 0 <= choice < len(flights):
                return flights[choice]
            else:
                print("Ungültige Auswahl. Bitte erneut versuchen.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

def main():
    print("Willkommen zur Flughafen-Ticket-Simulation!\n")

    flights = list_flights()
    blockchain = Blockchain()

    for idx, flight in enumerate(flights):
        print(f"{idx + 1}. {flight}")

    while True:
        selected_flight = select_flight(flights)
        passenger_name = input("Name des Passagiers: ").strip()

        if not passenger_name:
            print("Name darf nicht leer sein. Bitte erneut eingeben.")
            continue

        if PaymentProcessor.process_payment(selected_flight.price):
            ticket = Ticket(selected_flight, passenger_name)
            print("\n--- Dein Ticket ---")
            print(ticket)
            Logger.log(f"Buchung: {ticket.ticket_id} | Passagier: {passenger_name} | Flug: {selected_flight}")

            # 🛡 Ticket zur Blockchain hinzufügen
            block = blockchain.add_ticket(ticket)
            print("\nBlock hinzugefügt:")
            print(block)

        another = input("\nNoch ein Ticket buchen? (ja/nein): ").strip().lower()
        if another != 'ja':
            break

    print("\n--- Blockchain der Tickets ---")
    blockchain.display_chain()
    print("\nVielen Dank für deine Buchungen. Bis zum nächsten Mal!")

if __name__ == "__main__":
    main()