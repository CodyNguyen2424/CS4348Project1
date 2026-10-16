import sys
from datetime import datetime


def main():
    # Gives logger name of log file
    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <log_file_name>")
        return

    file_name = sys.argv[1]

    # Open file
    log_file = open(file_name, "a")

    while True:
        # Read users line 
        line = sys.stdin.readline()

        if line == "":
            break

        line = line.strip()

        if line == "QUIT":
            break

        # Ignore empty lines
        if line == "":
            continue

        # First word is action and rest is message
        parts = line.split(maxsplit=1)
        action = parts[0]

        message = ""
        if len(parts) > 1:
            message = parts[1]

        # Date format
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M")

        # Timestamp, action, and message
        log_entry = timestamp + " [" + action + "]"
        if message != "":
            log_entry = log_entry + " " + message

        log_file.write(log_entry + "\n")
        log_file.flush()

    log_file.close()

main()
