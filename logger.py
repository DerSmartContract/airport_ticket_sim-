## logger.py ##
import datetime

class Logger:
    LOG_FILE = "buchungs_log.txt"

    @staticmethod
    def log(message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        try:
            with open(Logger.LOG_FILE, "a", encoding="utf-8") as file:
                file.write(entry)
        except IOError as e:
            print(f"Fehler beim Schreiben des Logfiles: {e}")