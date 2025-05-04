import json
import os
from logger import Logger

def test_logger_writes_json(tmp_path):
    log_file = tmp_path / "test_log.json"

    # Logger soll in diese Datei schreiben
    Logger.LOG_FILE = str(log_file)

    # Beispiel-Logeintrag
    test_message = "Testbuchung erfolgreich."
    Logger.log(test_message, level="INFO")

    # Datei prüfen
    assert log_file.exists()

    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) > 0

    # JSON prüfen
    log_entry = json.loads(lines[0])
    assert log_entry["message"] == test_message
    assert log_entry["level"] == "INFO"
    assert "timestamp" in log_entry