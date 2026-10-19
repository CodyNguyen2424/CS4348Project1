# CS4348 Project 1

## How to Run

1. Clone repo
2. Make sure Python 3 is installed.
3. Run:

   `python3 driver.py test.log`

`driver.py` starts `logger.py` and `encryption.py` automatically. 
The file `test.log` stores program activity and will be created if it does not already exist.

## Menu

- **password** — Enter a new password or choose a string from history to use as a password.
- **encrypt** — Enter a new string or choose one from history to encrypt.
- **decrypt** — Enter a new string or choose one from history to decrypt.
- **history** — Display previously entered strings and successful encryption/decryption results.
- **quit** — Exit the program and stop both child processes.

When choosing from history, select an item by its number. Enter `0` to type a new string instead.

Input strings must contain letters only. Lowercase letters are converted to uppercase. Set a password before encrypting or decrypting. New passwords are not saved in history, and history is cleared when the program exits.

## Programs

- **driver.py** — Main program. Displays the menu, accepts user input, manages history, and communicates with the logger and encryption programs using pipes.
- **encryption.py** — Encrypts and decrypts strings using the Vigenère cipher. Receives `PASS`, `ENCRYPT`, `DECRYPT`, and `QUIT` commands from the driver.
- **logger.py** — Saves program commands and results to the chosen log file with timestamps. Password values are not directly logged.

## Devlog

- **devlog.md** — Notes about development sessions, changes, testing, and problems encountered.
