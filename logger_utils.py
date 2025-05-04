import json
from datetime import datetime
from typing import Optional, Union
from pathlib import Path

class Logger:
    LOG_FILE: str = "buchungs_log.txt"
    VALID_LEVELS = {"INFO", "ERROR", "WARNING", "DEBUG"}

    @staticmethod
    def log(
        message: str,
        level: str = "INFO",
        logfile: Optional[Union[str, Path]] = None,
        console_output: bool = True
    ) -> None:
        level = level.upper()
        if level not in Logger.VALID_LEVELS:
            raise ValueError(f"Ungültiger Log-Level: {level}. Erlaubt: {Logger.VALID_LEVELS}")

        log_entry = {
            "timestamp": datetime.now().isoformat(sep=' ', timespec='seconds'),
            "level": level,
            "message": message
        }

        log_line = json.dumps(log_entry, ensure_ascii=False)

        log_file_name = logfile if logfile else Logger.LOG_FILE
        if isinstance(log_file_name, Path):
            log_file_name = str(log_file_name)

        try:
            with open(log_file_name, "a", encoding="utf-8") as file:
                file.write(log_line + "\n")
                file.flush()
        except IOError as e:
            if console_output:
                print(f"Fehler beim Schreiben des Logfiles ({log_file_name}): {e}")

        if console_output:
            print(f"[{log_entry['timestamp']}] [{log_entry['level']}] {log_entry['message']}")