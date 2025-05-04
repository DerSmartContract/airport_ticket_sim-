# airport_ticket_sim-
Eine modulare, minimalistische Flughafen-Ticket-Simulation in Python. Inspiriert von der Eleganz und Unveränderlichkeit der Bitcoin-Blockchain. Features: Ticketbuchung, Zahlungsverarbeitung, Logging und eine verkettete Blockchain-Struktur für Ticket-Integrität.




Perfekt. Hier kommt deine README.md, technisch und optisch optimiert für GitHub und alle modernen Plattformen:

# Flughafen Ticket Simulation ✈️

**Version:** 1.0  
**Autor:** Dein Name (oder Teamname)  
**Lizenz:** MIT

---

## 📝 Projektbeschreibung

**Airport Ticket Simulation** ist eine modulare und minimalistische Python-Anwendung zur Simulation eines Flughafen-Ticketbuchungssystems.  
Inspiriert von den Grundprinzipien der Bitcoin-Blockchain vereint sie:

- Einfache Benutzerinteraktion
- Klare Datenstrukturen
- Unveränderliche Tickets durch kryptografische Verkettung

### Highlights:
- Ticketbuchung mit Fluginformationen
- Sichere Bezahlungssimulation
- Erstellung von unveränderlichen Tickets mit Hash-ID
- Verkettete Ticket-Blockchain für maximale Integrität
- Logging aller Buchungen mit Zeitstempel
- Fehlerbehandlung und benutzerfreundliche Interaktionen

---

## 📂 Projektstruktur

```plaintext
airport_ticket_sim/
├── flight.py             # Definition der Flight-Klasse
├── ticket.py             # Definition der Ticket-Klasse mit Hash-ID
├── payment.py            # Zahlungsabwicklung
├── logger.py             # Logging der Buchungen
├── blockchain.py         # TicketBlock-Klasse (Blockchain-Einzelblock)
├── blockchain_manager.py # Blockchain-Manager zur Verwaltung der Ticket-Kette
├── main.py               # Hauptprogramm (Benutzerinteraktion)
├── buchungs_log.txt      # Logdatei (wird automatisch erstellt)
├── data/                 # (Optional) Für spätere Erweiterungen
└── README.md             # Projektdokumentation



⸻

 Voraussetzungen
	•	Python 3.8 oder höher

Installation (optional):

pip install -r requirements.txt   # Momentan keine externen Bibliotheken nötig



⸻

 Verwendung

Starte das Hauptprogramm:

python main.py

Benutzerflow:
	1.	Flüge anzeigen lassen
	2.	Flug auswählen
	3.	Passagiernamen eingeben
	4.	Zahlung wird simuliert
	5.	Ticket wird erstellt und zur Blockchain hinzugefügt
	6.	Optional: Weitere Tickets buchen
	7.	Am Ende wird die gesamte Blockchain angezeigt

Alle Buchungen werden im buchungs_log.txt mit Zeitstempel gespeichert.

⸻

 Beispiel-Ausgabe

--- Dein Ticket ---
Ticket ID: 91f2...6a2b
Passenger: Max Mustermann
Flight: AB123: Berlin -> New York ($500.00)

Block hinzugefügt:
Block Hash: 47a5...be3f
Previous Hash: 0000...0000

Am Ende siehst du die gesamte Blockchain aller gebuchten Tickets.

⸻

 Technisches Design
	•	OOP: Alle Entitäten (Flight, Ticket, Payment, Blockchain) sind als Klassen umgesetzt.
	•	SHA-256 Hashing: Für die Erstellung unveränderlicher Ticket-IDs und Blockchain-Verkettung.
	•	Open/Closed Principle: Erweiterungen (z. B. Blockchain) ohne Änderung bestehender Dateien.
	•	Modularität: Klare Trennung von Verantwortlichkeiten in separaten Dateien.

⸻

 Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
Freie Nutzung, Änderung und Verteilung erlaubt.

⸻

 Beitrag leisten

Beiträge, Bug-Reports und Feature-Wünsche sind willkommen!
Bitte öffne einen Pull-Request oder erstelle ein Issue.

⸻

📞 Kontakt

Für Fragen oder Kooperationen: [deine.email@example.com]

⸻