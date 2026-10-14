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


# Test encryption and decryption
text = "HELLO"
key = "HELLO"

encrypted = encrypt_text(text, key)
print("Original:", text)
print("Encrypted:", encrypted)

decrypted = decrypt_text(encrypted, key)
print("Decrypted:", decrypted)
