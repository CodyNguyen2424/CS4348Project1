# 10-13-2026 10:23pm - Initial Entry
I have reviewed looked at the requirements for Project 1.
I will need at least 2 entries per session to record my thoughts.
There are 3 programs: a logger, an encryption program, and a driver.
The driver will use subprocesses and pipes to communicate with the other two programs.
As of right now, I am wondering where I should start and what would be the easiest program to begin with.

# 10-13-2026 11:08pm - Session 1 Start
I have created a repo on github and uploaded the project requirement files and given python code.
I have thought of a rough outline on how I want to go about this project.
I plan to begin with the logger, since it has the simplest functionality. 
After completing and testing it, I will work on the encryption program and then the driver.
I need it to accept a log filename, read messages from standard input, and write them with the required timestamps and action labels.

# 10-14-2026 12:45am - Session 1 End
I have created the logger.py program.
The program is supposed to read input and record it in a log file, which I am using test.log for testing.
I implemented a while loop to keep reading input, separated the action from the message, and added a date to each log entry.

However, I encountered some problems, and the program is not working correctly yet.
Some of the issues include the log file being overwritten when the program starts again, the date not displaying in the required format, and the program not stopping when QUIT is entered. 
I also noticed that entering an empty line causes an error. 
I will need to fix these problems before the logger is complete.

# 10-14-2026 10:14am - Session 2 Start
During my last session, I created the logger.py program, but there were several problems.
The program is supposed to read input from the user and record it in test.log.
I think some of the problems are caused by how I am opening the file and how I am checking the input in the while loop.
It should break the while loop when the user inputs QUIT.
The timestamp format bug should just be a simple syntax error on my part.
I plan to fix these bugs and finish logger.py in this session.

# 10-14-2026 10:57am - Session 2 End
I finished fixing the problems with logger.py.
One of the problems was that the log file was being overwritten every time I ran the program. 
This was because I was using "w" when opening the file. 
I changed it to "a" so that new entries would be added without deleting the previous ones.
I fixed the syntax of the date to be in the right format.
I also fixed the while loop by changing continue to break when QUIT is entered.
The last problem was that entering an empty line would cause an error because the program tried to access an empty list.
I fixed this by checking for empty input before splitting the line.
The logger should now be working as intended.

For my next session, I plan to start working on encryption.py. 
I want to work on this next because it should be easier to test the encryption and decryption functions separately before connecting everything together using the driver program.

# 10-14-2026 4:06pm - Session 3 Start
Now that the logger works, I plan to start the encryption program, encryption.py.
This program will encrypt and decrypt strings using the Vigenere cipher.

I plan to use the Vigenere cipher like how it is in the wiki given to us in the project instructions.
From what I see, the cypher uses a key to shift each letter of the string.
I will need to convert the letters to numbers, do some calculation, and then convert them back to letters.
Encryption should work by adding the shift calculation and decryption should work by subtracting the shift calculation.

For this session, I plan to create encryption.py and implement the functions for encrypting and decrypting strings. 
I want to focus on getting the Vigenère cipher calculations working.

# 10-14-2026 4:58pm - Session 3 End
I created encryption.py and implemented the encryption and decryption functions using the Vigenère cipher.
I based it off of the wiki page given to us.
The cipher uses a key to shift each letter in the original string to create an encrypted string.

I created an alphabet string containing all the uppercase letters from A to Z. 
Each letter has a position from 0 to 25. 
For encryption, I used the equation C = (P + K) % 26.
P is the original letter's position, K is the key letter's position, and C is the encrypted letter's position. 
For decryption, I used P = (C - K) % 26 to reverse the process. 
I also used the modulo operator to repeat the key when the string is longer than the password.

After implementing both functions, I tested the program using HELLO as both the original string and the key. 
When I ran encryption.py, the program encrypted HELLO into OIWWC. 
It then decrypted OIWWC back into HELLO using the same key. 
The test worked, so both functions appear to be working correctly.

For my next session, I plan to implement the commands for the encryption program, including PASS, ENCRYPT, DECRYPT, and QUIT.