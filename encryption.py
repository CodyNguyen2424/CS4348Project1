import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt_text(text, key):
    encrypted_text = ""

    # Go through each letter in text
    for i in range(len(text)):
        letter = text[i]

        # Find letter's number in alphabet
        letter_number = alphabet.index(letter)

        # Repeat key if text is longer than key
        key_position = i % len(key)
        key_letter = key[key_position]
        key_number = alphabet.index(key_letter)

        # Add letter and key numbers
        new_number = (letter_number + key_number) % 26

        # Convert number back into a letter
        new_letter = alphabet[new_number]

        encrypted_text = encrypted_text + new_letter

    return encrypted_text


def decrypt_text(text, key):
    decrypted_text = ""

    # Go through each letter in text
    for i in range(len(text)):
        letter = text[i]

        # Find letter's number in alphabet
        letter_number = alphabet.index(letter)

        # Repeat key if text is longer than key
        key_position = i % len(key)
        key_letter = key[key_position]
        key_number = alphabet.index(key_letter)

        # Subtract key number from letter number
        new_number = (letter_number - key_number) % 26

        # Convert number back into a letter
        new_letter = alphabet[new_number]

        decrypted_text = decrypted_text + new_letter

    return decrypted_text


def main():
    current_key = ""

    while True:
        line = sys.stdin.readline()

        if line == "":
            break

        line = line.strip()

        if line == "":
            continue

        # Separate command and argument
        parts = line.split(maxsplit=1)
        command = parts[0]

        argument = ""
        if len(parts) > 1:
            argument = parts[1]

        if command == "QUIT":
            break

        elif command == "PASS":
            if argument == "":
                print("ERROR Password cannot be empty", flush=True)
            else:
                current_key = argument
                print("RESULT", flush=True)

        elif command == "ENCRYPT":
            if argument == "":
                print("ERROR Text cannot be empty", flush=True)
            else:
                result = encrypt_text(argument, current_key)
                print(result, flush=True)
                current_key = ""

        elif command == "DECRYPT":
            if current_key == "":
                print("ERROR Password not set", flush=True)
            elif argument == "":
                print("ERROR Text cannot be empty", flush=True)
            else:
                result = decrypt_text(argument, current_key)
                print("RESULT " + result, flush=True)

        else:
            print("ERROR Unknown command", flush=True)


main()
