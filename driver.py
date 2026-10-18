import sys
from subprocess import Popen, PIPE


def show_history(history):
    # Show all strings saved during this run
    if len(history) == 0:
        print("History is empty.")
    else:
        print("\nHistory:")
        for i in range(len(history)):
            print(str(i + 1) + ". " + history[i])


def is_valid_string(text):
    # Check for empty input
    if text == "":
        print("String cannot be empty.")
        return False

    # Allow uppercase letters only
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in text:
        if letter not in alphabet:
            print("Only letters are allowed.")
            return False

    return True


def enter_new_string(history, is_password):
    text = input("Enter a new string: ").upper()

    if is_valid_string(text) == False:
        return None

    # Save new strings except passwords
    if is_password == False:
        history.append(text)

    return text


def choose_string(history, is_password):
    while True:
        print("\n1. Enter a new string")
        print("2. Select a string from history")

        option = input("Choose an option: ").strip()

        if option == "1":
            return enter_new_string(history, is_password)

        elif option == "2":
            if len(history) == 0:
                print("History is empty. Please enter a new string.")
            else:
                show_history(history)
                print("0. Enter a new string instead")

                number = input("Select a number: ").strip()

                if number == "0":
                    return enter_new_string(history, is_password)

                elif number.isdigit():
                    index = int(number) - 1

                    if index >= 0 and index < len(history):
                        return history[index]
                    else:
                        print("Invalid history number.")
                else:
                    print("Invalid history number.")

        else:
            print("Invalid option. Please enter 1 or 2.")


def send_encryption_command(encryption, command):
    # Send command to encryption process
    encryption.stdin.write(command + "\n")
    encryption.stdin.flush()

    # Read response from encryption process
    response = encryption.stdout.readline().strip()
    return response


def send_log_message(logger, message):
    # Send message to logger process
    logger.stdin.write(message + "\n")
    logger.stdin.flush()


def main():
    # User gives name of log file
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file_name>")
        return

    file_name = sys.argv[1]

    # Start logger as a separate process
    logger = Popen(
        [sys.executable, "logger.py", file_name],
        stdin=PIPE,
        stdout=PIPE,
        text=True
    )

    # Start encryption as another process
    encryption = Popen(
        [sys.executable, "encryption.py"],
        stdin=PIPE,
        stdout=PIPE,
        text=True
    )

    send_log_message(logger, "START Driver started.")

    # History exists only while driver is running
    history = []

    # Menu
    while True:
        print("\nMenu:")
        print("password - Select a password")
        print("encrypt  - Select a string to encrypt")
        print("decrypt  - Select a string to decrypt")
        print("history  - Show saved strings")
        print("quit     - Exit the program")

        command = input("Enter a command: ").strip().lower()

        if command == "password":
            # Log password command without password
            send_log_message(logger, "PASSWORD Password command selected.")

            password = choose_string(history, True)
            if password is not None:
                # Set password in encryption process
                response = send_encryption_command(encryption, "PASS " + password)
                print("Password response:", response)
                send_log_message(logger, response)
            else:
                send_log_message(logger, "ERROR Invalid password.")

        elif command == "encrypt":
            send_log_message(logger, "ENCRYPT Encrypt command selected.")

            text = choose_string(history, False)
            if text is not None:
                # Encrypt selected string
                response = send_encryption_command(encryption, "ENCRYPT " + text)
                print("Encryption response:", response)
                send_log_message(logger, response)

                # Save successful result
                parts = response.split(maxsplit=1)
                if len(parts) == 2 and parts[0] == "RESULT":
                    history.append(parts[1])
            else:
                send_log_message(logger, "ERROR Invalid encryption input.")

        elif command == "decrypt":
            send_log_message(logger, "DECRYPT Decrypt command selected.")

            text = choose_string(history, False)
            if text is not None:
                # Decrypt selected string
                response = send_encryption_command(encryption, "DECRYPT " + text)
                print("Decryption response:", response)
                send_log_message(logger, response)

                # Save successful result
                parts = response.split(maxsplit=1)
                if len(parts) == 2 and parts[0] == "RESULT":
                    history.append(parts[1])
            else:
                send_log_message(logger, "ERROR Invalid decryption input.")

        elif command == "history":
            send_log_message(logger, "HISTORY History requested.")
            show_history(history)
            send_log_message(logger, "RESULT History displayed.")

        elif command == "quit":
            send_log_message(logger, "QUIT User requested exit.")
            send_log_message(logger, "RESULT Program exiting.")
            break

        else:
            print("Invalid command. Please choose a command from the menu.")
            send_log_message(logger, "COMMAND Invalid menu command.")
            send_log_message(logger, "ERROR Unknown menu command.")

    # Stop encryption process
    encryption.stdin.write("QUIT\n")
    encryption.stdin.flush()

    # Log exit before stopping logger
    send_log_message(logger, "EXIT Driver stopped.")
    logger.stdin.write("QUIT\n")
    logger.stdin.flush()

    encryption.stdin.close()
    logger.stdin.close()

    # Wait for both processes to stop
    encryption.wait()
    logger.wait()

    encryption.stdout.close()
    logger.stdout.close()

    print("Both child processes have stopped.")

main()