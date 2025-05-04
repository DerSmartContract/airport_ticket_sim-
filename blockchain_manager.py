from blockchain import TicketBlock

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_ticket(self, ticket):
        previous_hash = self.chain[-1].block_hash if self.chain else "0" * 64
        block = TicketBlock(ticket, previous_hash)
        self.chain.append(block)
        return block

    def display_chain(self):
        for idx, block in enumerate(self.chain):
            print(f"\n--- Block {idx + 1} ---")
            print(block)