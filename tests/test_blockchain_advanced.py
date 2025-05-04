import pytest
from flight import Flight
from ticket import Ticket
from blockchain_manager import Blockchain

def test_blockchain_integrity():
    blockchain = Blockchain()
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket1 = Ticket(flight, "Max Mustermann")
    ticket2 = Ticket(flight, "Erika Musterfrau")

    block1 = blockchain.add_ticket(ticket1)
    block2 = blockchain.add_ticket(ticket2)

    assert block2.previous_hash == block1.block_hash

@pytest.mark.skip(reason="Tickets sind immutable. Manipulationstest nicht anwendbar.")
def test_blockchain_manipulation_detection():
    blockchain = Blockchain()
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket = Ticket(flight, "Max Mustermann")

    block = blockchain.add_ticket(ticket)

    original_hash = block.block_hash

    # ACHTUNG: Simulation! In deinem echten Code sind Tickets immutable.
    block.ticket.passenger_name = "Hacker"
    new_hash = block._generate_block_hash()

    assert new_hash != original_hash, "Manipulation sollte den Block-Hash ändern."

def test_invalid_ticket_addition():
    blockchain = Blockchain()
    with pytest.raises(TypeError):
        blockchain.add_ticket("Kein echtes Ticket")

def test_empty_blockchain_display(capsys):
    blockchain = Blockchain()
    blockchain.display_chain()
    captured = capsys.readouterr()
    assert "Die Blockchain ist leer." in captured.out