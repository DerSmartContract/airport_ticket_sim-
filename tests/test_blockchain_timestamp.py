import os
from blockchain_manager import Blockchain
from flight import Flight
from ticket import Ticket

def test_timestamp_persistence(tmp_path):
    # Schritt 1: Blockchain erstellen und Ticket hinzufügen
    blockchain = Blockchain()
    flight = Flight("LH123", "Berlin", "London", 300)
    ticket = Ticket(flight, "Max Mustermann")
    block = blockchain.add_ticket(ticket)

    # Timestamp des ersten Blocks merken
    original_timestamp = block.timestamp

    # Schritt 2: Blockchain speichern
    file_path = tmp_path / "blockchain_timestamp_test.json"
    blockchain.save_chain_to_file(filename=str(file_path))

    # Schritt 3: Neue Blockchain laden
    new_blockchain = Blockchain()
    new_blockchain.load_chain_from_file(filename=str(file_path))

    # Schritt 4: Timestamp überprüfen
    assert len(new_blockchain.chain) == 1

    loaded_block = new_blockchain.chain[0]
    assert loaded_block.timestamp == original_timestamp

    # Sicherheit: Blockchain weiterhin gültig
    assert new_blockchain.is_chain_valid()