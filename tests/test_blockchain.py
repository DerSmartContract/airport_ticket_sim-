from flight import Flight
from ticket import Ticket
from blockchain_manager import Blockchain

def test_blockchain_add_ticket():
    blockchain = Blockchain()
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket = Ticket(flight, "Max Mustermann")

    block = blockchain.add_ticket(ticket)
    assert block.block_hash is not None
    assert block.ticket == ticket

def test_blockchain_chain_length():
    blockchain = Blockchain()
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket1 = Ticket(flight, "Max Mustermann")
    ticket2 = Ticket(flight, "Erika Musterfrau")

    blockchain.add_ticket(ticket1)
    blockchain.add_ticket(ticket2)

    assert len(blockchain.chain) == 2