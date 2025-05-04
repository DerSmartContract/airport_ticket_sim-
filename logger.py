import json
from datetime import datetime

class Logger:
    LOG_FILE = "buchungs_log.txt"

    @staticmethod
    def log(message: str, level: str = "INFO") -> None:
        """
        Loggt eine Nachricht im JSON-Format mit Zeitstempel und Level.
        """
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level.upper(),
            "message": message
        }

        log_line = json.dumps(log_entry, ensure_ascii=False)

        try:
            with open(Logger.LOG_FILE, "a", encoding="utf-8") as file:
                file.write(log_line + "\n")
        except IOError as e:
            print(f"Fehler beim Schreiben des Logfiles: {e}")

        # Optional: auch in der Konsole ausgeben
        print(f"[{log_entry['timestamp']}] [{log_entry['level']}] {log_entry['message']}")