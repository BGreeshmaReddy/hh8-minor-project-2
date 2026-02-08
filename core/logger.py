from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "deletion_log.txt")

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} | {message}\n"

    print("📝 LOGGING:", log_line.strip())  # <-- PROOF

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)
        f.flush()
