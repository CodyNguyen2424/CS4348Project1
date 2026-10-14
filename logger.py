
import sys
from datetime import datetime


def main():
    # Gives logger the name of the log file
    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <log_file_name>")
        return

    file_name = sys.argv[1]

    # Open file
    log_file = open(file_name, "w")

    while True:
        # Read users line 
        line = sys.stdin.readline()

        line = line.strip()

        if line == "QUIT":
            continue

        # First word is the action and rest is the message
        parts = line.split(maxsplit=1)
        action = parts[0]

        message = ""
        if len(parts) > 1:
            message = parts[1]

        # Date format
        current_time = datetime.now()
        timestamp = current_time.strftime("%m-%d-%Y")

        # Timestamp, action, and message
        log_entry = timestamp + " [" + action + "]"
        if message != "":
            log_entry = log_entry + " " + message

        log_file.write(log_entry + "\n")
        log_file.flush()

    log_file.close()


main()
