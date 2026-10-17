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


def enter_new_string(history, is_password):
    text = input("Enter a new string: ").strip()

    if text == "":
        print("String cannot be empty.")
        return None

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

    logger.stdin.write("START Driver started.\n")
    logger.stdin.flush()

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
            password = choose_string(history, True)
            if password is not None:
                print("Password selected. Command processing comes in Session 8.")

        elif command == "encrypt":
            text = choose_string(history, False)
            if text is not None:
                print("Selected string:", text)
                print("Encryption will be connected in Session 8.")

        elif command == "decrypt":
            text = choose_string(history, False)
            if text is not None:
                print("Selected string:", text)
                print("Decryption will be connected in Session 8.")

        elif command == "history":
            show_history(history)

        elif command == "quit":
            break

        else:
            print("Invalid command. Please choose a command from the menu.")

    # Tell both child processes to stop
    encryption.stdin.write("QUIT\n")
    encryption.stdin.flush()

    logger.stdin.write("EXIT Driver stopped.\n")
    logger.stdin.write("QUIT\n")
    logger.stdin.flush()

    # Wait until both processes have stopped
    encryption.wait()
    logger.wait()

    # Close pipes
    encryption.stdin.close()
    encryption.stdout.close()
    logger.stdin.close()
    logger.stdout.close()

    print("Both child processes have stopped.")


main()
