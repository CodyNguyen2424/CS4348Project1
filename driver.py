import sys
from subprocess import Popen, PIPE


def main():
    # User gives name of log file
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file_name>")
        return

    file_name = sys.argv[1]

    # Start logger as separate process
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

    # Send message to logger
    logger.stdin.write("START Driver started.\n")
    logger.stdin.flush()

    # Test sending a password to encryption program
    encryption.stdin.write("PASS HELLO\n")
    encryption.stdin.flush()

    # Wait for encryption program to answer
    response = encryption.stdout.readline().strip()
    print("Password response:", response)

    # Tell logger what happened
    logger.stdin.write("PASS Password command sent.\n")
    logger.stdin.write(response + "\n")
    logger.stdin.flush()

    # Test sending an encryption command
    encryption.stdin.write("ENCRYPT HELLO\n")
    encryption.stdin.flush()

    # Read encrypted result from other process
    response = encryption.stdout.readline().strip()
    print("Encryption response:", response)

    logger.stdin.write("ENCRYPT Encryption command sent.\n")
    logger.stdin.write(response + "\n")
    logger.stdin.flush()

    # Test sending a decryption command
    encryption.stdin.write("DECRYPT OIWWC\n")
    encryption.stdin.flush()

    # Read the decrypted result
    response = encryption.stdout.readline().strip()
    print("Decryption response:", response)

    logger.stdin.write("DECRYPT Decryption command sent.\n")
    logger.stdin.write(response + "\n")
    logger.stdin.flush()

    # Tell both child processes to stop
    encryption.stdin.write("QUIT\n")
    encryption.stdin.flush()

    logger.stdin.write("EXIT Driver finished testing.\n")
    logger.stdin.write("QUIT\n")
    logger.stdin.flush()

    encryption.wait()
    logger.wait()

    # Close pipes
    encryption.stdin.close()
    encryption.stdout.close()
    logger.stdin.close()
    logger.stdout.close()

    print("Both child processes have stopped.")


main()
