import sys
import os
import json
import hashlib

# 🔥 WICHTIG: Hauptpfad hinzufügen, damit flight, ticket etc. gefunden werden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flight import Flight
from ticket import Ticket
from blockchain import TicketBlock

def diagnose_blockchain(filename="blockchain.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Fehler beim Laden der Blockchain-Datei: {e}")
        return

    previous_chain_hash = "0" * 64
    print(f"Analysiere {len(data)} Blöcke...\n")

    error_count = 0  # Fehlerzähler

    for i, entry in enumerate(data):
        print(f"--- Block {i + 1} ---")

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

        # Berechneter Block-Hash
        timestamp = entry["timestamp"]
        data_str = f"{ticket.ticket_id}|{entry['previous_hash']}|{timestamp}".encode("utf-8")
        calculated_block_hash = hashlib.sha256(data_str).hexdigest()

        stored_block_hash = entry["block_hash"]

        if calculated_block_hash != stored_block_hash:
            print(f"❌ Unterschied beim Block-Hash!")
            print(f"Gespeichert: {stored_block_hash}")
            print(f"Berechnet : {calculated_block_hash}")
            error_count += 1
        else:
            print("✔ Block-Hash stimmt überein.")

        # Chain-Hash prüfen (falls vorhanden)
        chain_hash_stored = entry.get("chain_hash")
        if chain_hash_stored:
            chain_data = f"{previous_chain_hash}|{calculated_block_hash}".encode("utf-8")
            calculated_chain_hash = hashlib.sha256(chain_data).hexdigest()

            if calculated_chain_hash != chain_hash_stored:
                print(f"❌ Unterschied beim Chain-Hash!")
                print(f"Gespeichert: {chain_hash_stored}")
                print(f"Berechnet : {calculated_chain_hash}")
                error_count += 1
            else:
                print("✔ Chain-Hash stimmt überein.")

            previous_chain_hash = chain_hash_stored
        else:
            print("(Chain-Hash nicht gespeichert – Block älter?)")

        print()

    # Zusammenfassung
    if error_count == 0:
        print("✅ Alle Hashes stimmen überein. Keine Fehler gefunden.")
    else:
        print(f"❌ Es wurden {error_count} Fehler gefunden.")

if __name__ == "__main__":
    diagnose_blockchain()