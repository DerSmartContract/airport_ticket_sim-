from blockchain import TicketBlock
from ticket import Ticket
from flight import Flight
from typing import List, Optional
import json
from datetime import datetime
import hashlib
import os

class Blockchain:
    def __init__(self) -> None:
        self.chain: List[TicketBlock] = []

    def add_ticket(self, ticket: Ticket) -> TicketBlock:
        if not isinstance(ticket, Ticket):
            raise TypeError("Nur Ticket-Objekte können zur Blockchain hinzugefügt werden.")

        previous_hash = self.chain[-1].block_hash if self.chain else "0" * 64
        previous_chain_hash = self.chain[-1].chain_hash if self.chain else "0" * 64

        block = TicketBlock(ticket, previous_hash, previous_chain_hash)
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
        """
        Prüft die Integrität der Blockchain inkl. Chain-Hash.
        """
        if not self.chain:
            print("Die Blockchain ist leer. Nichts zu validieren.")
            return True

        previous_chain_hash = "0" * 64
        for i, block in enumerate(self.chain):
            # Block-Hash prüfen
            expected_block_hash = block._generate_block_hash()
            if block.block_hash != expected_block_hash:
                print(f"Fehler: Block {i+1} - Block-Hash stimmt nicht überein.")
                return False

            # Chain-Hash prüfen
            expected_chain_hash = block._generate_chain_hash(previous_chain_hash)
            if block.chain_hash != expected_chain_hash:
                print(f"Fehler: Block {i+1} - Chain-Hash stimmt nicht überein.")
                return False

            # Previous Hash prüfen
            if i > 0 and block.previous_hash != self.chain[i - 1].block_hash:
                print(f"Fehler: Block {i+1} - previous_hash inkonsistent.")
                return False

            previous_chain_hash = block.chain_hash

        return True

    def save_chain_to_file(self, filename: str = "blockchain.json") -> None:
        """
        Speichert die Blockchain in eine JSON-Datei und erzeugt einen Integritätshash.
        """
        data = []
        for block in self.chain:
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
                "chain_hash": block.chain_hash,
                "timestamp": block.timestamp
            })

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            # 🔒 Datei-Hash berechnen und speichern
            file_hash = self._calculate_file_hash(filename)
            with open("blockchain_hash.txt", "w") as hfile:
                hfile.write(file_hash)

        except IOError as e:
            print(f"Fehler beim Speichern der Blockchain: {e}")

    def load_chain_from_file(self, filename: str = "blockchain.json") -> None:
        """
        Lädt die Blockchain aus einer JSON-Datei und prüft den Datei-Hash und die Chain-Hash-Verkettung.
        """
        try:
            # 🔒 Datei-Hash prüfen
            self._verify_file_hash(filename)

            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.chain = []
            previous_chain_hash = "0" * 64

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

                block = TicketBlock(ticket, entry["previous_hash"], previous_chain_hash)
                block.timestamp = entry.get("timestamp") or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Block- und Chain-Hashes prüfen
                recalculated_block_hash = block._generate_block_hash()
                if recalculated_block_hash != entry["block_hash"]:
                    raise ValueError(
                        f"Block-Hash stimmt nicht überein (Ticket-ID: {ticket.ticket_id})."
                    )

                recalculated_chain_hash = block._generate_chain_hash(previous_chain_hash)
                if recalculated_chain_hash != entry["chain_hash"]:
                    raise ValueError(
                        f"Chain-Hash stimmt nicht überein (Ticket-ID: {ticket.ticket_id})."
                    )

                block.block_hash = entry["block_hash"]
                block.chain_hash = entry["chain_hash"]
                self.chain.append(block)
                previous_chain_hash = block.chain_hash

        except FileNotFoundError:
            print("Keine bestehende Blockchain-Datei gefunden. Neue Blockchain wird erstellt.")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Fehler beim Laden der Blockchain: {e}")

    # 🔥 Hilfsmethoden:

    def _calculate_file_hash(self, filename: str) -> str:
        """
        Berechnet den SHA-256-Hash einer Datei.
        """
        sha256 = hashlib.sha256()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _verify_file_hash(self, filename: str) -> None:
        """
        Prüft, ob der gespeicherte Hash mit dem aktuellen Dateiinhalt übereinstimmt.
        """
        if not os.path.exists("blockchain_hash.txt"):
            print("Kein gespeicherter Blockchain-Hash gefunden. Integritätsprüfung übersprungen.")
            return

        with open("blockchain_hash.txt", "r") as hfile:
            saved_hash = hfile.read().strip()

        current_hash = self._calculate_file_hash(filename)

        if saved_hash != current_hash:
            raise ValueError("Blockchain-Datei wurde verändert oder ist beschädigt (Hash stimmt nicht überein).")

    def get_chain_length(self) -> int:
        return len(self.chain)

    def get_last_block(self) -> Optional[TicketBlock]:
        return self.chain[-1] if self.chain else None

    def get_block_by_ticket_id(self, ticket_id: str) -> Optional[TicketBlock]:
        for block in self.chain:
            if block.ticket.ticket_id == ticket_id:
                return block
        return None