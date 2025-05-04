import hashlib

class TicketBlock:
    def __init__(self, ticket, previous_hash="0" * 64):
        self.ticket = ticket
        self.previous_hash = previous_hash
        self.block_hash = self._generate_block_hash()

    def _generate_block_hash(self):
        data = f"{self.ticket.ticket_id}{self.previous_hash}".encode()
        return hashlib.sha256(data).hexdigest()

    def __str__(self):
        return (f"Block Hash: {self.block_hash}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"{self.ticket}")