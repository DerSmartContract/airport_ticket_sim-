from blockchain import TicketBlock
from ticket import Ticket
from typing import List
import json
from datetime import datetime

class Blockchain:
    def __init__(self) -> None:
        self.chain: List[TicketBlock] = []

    def add_ticket(self, ticket: Ticket) -> TicketBlock:
        if not isinstance(ticket, Ticket):
            raise TypeError("Nur Ticket-Objekte können zur Blockchain hinzugefügt werden.")

        previous_hash = self.chain[-1].block_hash if self.chain else "0" * 64
        block = TicketBlock(ticket, previous_hash)
        self.chain.append(block)
        return block

    def display_chain(self) -> None:
        if not self.chain:
            print("Die Blockchain ist leer.")
            return

        for idx, block in enumerate(self.chain, start=1):
            print(f"\n--- Block {idx} ---")
            print(block)

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Hash des vorherigen Blocks muss stimmen
            if current.previous_hash != previous.block_hash:
                return False

            # Block-Hash muss mit den Daten übereinstimmen
            recalculated_hash = current._generate_block_hash()
            if current.block_hash != recalculated_hash:
                return False

        return True

    def save_chain_to_file(self, filename: str = "blockchain.json") -> None:
        data = []
        for block in self.chain:
            # Falls der Block keinen timestamp hat (alte Blöcke), setzen wir ihn jetzt
            if not hasattr(block, "timestamp") or block.timestamp is None:
                block.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            data.append({
                "ticket_id": block.ticket.ticket_id,
                "passenger_name": block.ticket.passenger_name,
                "flight_number": block.ticket.flight.flight_number,
                "origin": block.ticket.flight.origin,
                "destination": block.ticket.flight.destination,
                "price": block.ticket.flight.price,
                "previous_hash": block.previous_hash,
                "block_hash": block.block_hash,
                "timestamp": block.timestamp  # NEU: Zeitstempel speichern
            })
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_chain_from_file(self, filename: str = "blockchain.json") -> None:
        from blockchain import TicketBlock
        from flight import Flight
        from ticket import Ticket

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.chain = []  # leere Chain neu aufbauen

            for entry in data:
                flight = Flight(
                    flight_number=entry["flight_number"],
                    origin=entry["origin"],
                    destination=entry["destination"],
                    price=entry["price"]
                )
                ticket = Ticket(
                    flight=flight,
                    passenger_name=entry["passenger_name"]
                )

                block = TicketBlock(ticket, entry["previous_hash"])

                # Timestamp übernehmen oder generieren (Kompatibilität zu alten Dateien)
                block.timestamp = entry.get("timestamp")
                if block.timestamp is None:
                    block.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Hash neu berechnen mit geladenem oder neuem timestamp
                recalculated_hash = block._generate_block_hash()

                if recalculated_hash != entry["block_hash"]:
                    raise ValueError("Block-Hash stimmt nicht mit gespeicherten Daten überein.")

                block.block_hash = entry["block_hash"]  # gespeicherten Hash übernehmen
                self.chain.append(block)

        except FileNotFoundError:
            print("Keine bestehende Blockchain-Datei gefunden. Neue Blockchain wird erstellt.")