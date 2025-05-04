import hashlib
import datetime
from ticket import Ticket

class TicketBlock:
    def __init__(self, ticket: Ticket, previous_hash: str = "0" * 64) -> None:
        if not isinstance(ticket, Ticket):
            raise TypeError("ticket muss vom Typ Ticket sein.")
        if not isinstance(previous_hash, str) or len(previous_hash) != 64:
            raise ValueError("previous_hash muss ein 64-stelliger SHA-256 Hash sein.")

        self.ticket = ticket
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.block_hash = self._generate_block_hash()

    def _generate_block_hash(self) -> str:
        data = f"{self.ticket.ticket_id}|{self.previous_hash}|{self.timestamp}".encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def __str__(self) -> str:
        return (
            f"Block Hash: {self.block_hash}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Timestamp: {self.timestamp}\n"
            f"{self.ticket}"
        )