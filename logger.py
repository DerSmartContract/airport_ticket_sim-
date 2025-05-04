import datetime

class Logger:
    @staticmethod
    def log(message):
        with open("buchungs_log.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")