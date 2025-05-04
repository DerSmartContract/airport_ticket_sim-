import json
from logger_utils import Logger

def test_logger_writes_info_json(tmp_path):
    log_file = tmp_path / "test_log.json"

    original_log_file = Logger.LOG_FILE
    Logger.LOG_FILE = str(log_file)

    try:
        test_message = "Testbuchung erfolgreich."
        Logger.log(test_message, level="INFO", console_output=False)

        assert log_file.exists()

        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) > 0

        log_entry = json.loads(lines[0])
        assert log_entry["message"] == test_message
        assert log_entry["level"] == "INFO"
        assert "timestamp" in log_entry

    finally:
        Logger.LOG_FILE = original_log_file

def test_logger_writes_error_json(tmp_path):
    log_file = tmp_path / "error_log.json"

    original_log_file = Logger.LOG_FILE
    Logger.LOG_FILE = str(log_file)

    try:
        test_message = "Testfehler aufgetreten."
        Logger.log(test_message, level="ERROR", console_output=False)

        assert log_file.exists()

        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        assert len(lines) > 0

        log_entry = json.loads(lines[0])
        assert log_entry["message"] == test_message
        assert log_entry["level"] == "ERROR"
        assert "timestamp" in log_entry

    finally:
        Logger.LOG_FILE = original_log_file

def test_logger_invalid_level(tmp_path):
    log_file = tmp_path / "test_invalid_level_log.json"

    try:
        Logger.log(
            "Ungültiger Level-Test",
            level="INVALID",
            logfile=log_file,
            console_output=False
        )
        assert False, "Logger hat einen ungültigen Level akzeptiert."
    except ValueError as e:
        assert "Ungültiger Log-Level" in str(e)

def test_logger_console_output(capsys, tmp_path):
    """
    Testet, ob die Logger-Ausgabe in der Konsole erscheint.
    """
    log_file = tmp_path / "console_test_log.json"
    test_message = "Konsole-Ausgabe-Test."

    Logger.log(test_message, level="INFO", logfile=log_file, console_output=True)

    captured = capsys.readouterr()

    assert test_message in captured.out
    assert "INFO" in captured.out

    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    assert len(lines) > 0
    log_entry = json.loads(lines[0])
    assert log_entry["message"] == test_message