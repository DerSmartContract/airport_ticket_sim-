import os
from blockchain_manager import Blockchain
from flight import Flight
from ticket import Ticket

def test_blockchain_save_and_load(tmp_path):
    # Vorbereiten: Blockchain mit einem Ticket erstellen
    blockchain = Blockchain()
    flight = Flight("AB123", "Berlin", "New York", 500)
    ticket = Ticket(flight, "Max Mustermann")
    blockchain.add_ticket(ticket)

    # Speichern in eine temporäre Datei
    file_path = tmp_path / "blockchain_test.json"
    blockchain.save_chain_to_file(filename=str(file_path))

    # Neue Blockchain laden
    new_blockchain = Blockchain()
    new_blockchain.load_chain_from_file(filename=str(file_path))

    # Tests: Chain sollte gleich sein
    assert len(new_blockchain.chain) == 1

    loaded_block = new_blockchain.chain[0]
    assert loaded_block.ticket.passenger_name == "Max Mustermann"
    assert loaded_block.ticket.flight.flight_number == "AB123"

    # Integrität prüfen
    assert new_blockchain.is_chain_valid()

def test_load_nonexistent_file(tmp_path):
    blockchain = Blockchain()
    file_path = tmp_path / "nonexistent.json"

    # Sollte KEIN Fehler sein, sondern einfach eine leere Blockchain
    blockchain.load_chain_from_file(filename=str(file_path))
    assert len(blockchain.chain) == 0