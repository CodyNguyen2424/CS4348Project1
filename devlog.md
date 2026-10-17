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

# 10-15-2026 2:47pm - Session 4 Start
Now that encryption and decryption are working, I plan to implement the command processing for encryption.py.
I need to implement the PASS, ENCRYPT, DECRYPT, and QUIT commands.
The PASS command should store the current passkey so that the program can use it for encryption and decryption. 
The ENCRYPT and DECRYPT commands will call the functions I created in the previous session. 
I also need to make the program return RESULT when a command succeeds and ERROR when something goes wrong.

I plan to use a while loop to continuously read commands from standard input like how I implemented the logger. 
The program should separate the command from its argument.
It should perform the correct operation depending on the command entered. 
I will also need to make sure the program stops when it receives QUIT. 
My goal for this session is to get the encryption program responding to commands.

# 10-15-2026 3:56pm - Session 4 End
I updated encryption.py to handle the PASS, ENCRYPT, DECRYPT, and QUIT commands. 
I added a main function with a while loop that continuously reads commands from standard input. T
he program separates the command from its argument and uses if statements to determine what to do. 
I also added a current_key variable to store the password and made the program return RESULT or ERROR depending on the command.

There are several bugs and the program is not working as intended yet.
One problem is that the program forgets the password after encrypting a string. 
Another problem is that trying to encrypt a string without setting a password causes a ZeroDivisionError.
I also noticed that the ENCRYPT command only prints the encrypted string instead of including RESULT before it.

I plan to fix these problems and test the encryption program later in another session.

# 10-15-2026 8:28pm - Session 5 Start
There are several bugs that is preventing encryption.py from working correctly.
One problem was that the program forgot the password after encrypting a string.
Another problem was that trying to encrypt a string without setting a password caused a ZeroDivisionError. 
I think this happens because the program tries to use an empty key. 
I plan to add an if statement to check whether a password has been set before calling the encryption function. 
I also saw that the ENCRYPT command only prints the encrypted string instead of including RESULT before it. 
This should be a simple fix by changing the print statement.

I plan to fix these bugs and finish encryption.py. 
After making the changes, I want to test the program with different passwords, longer strings, and repeating keys.

# 10-15-2026 9:54pm - Session 5 End
I fixed the bugs from my previous session in encryption.py. 
The first problem was that the program would forget the password after encrypting a string. 
I fixed this by removing the line that reset current_key to an empty string after encryption. 

The second problem was that trying to encrypt a string without setting a password caused a ZeroDivisionError. 
I fixed this by adding an if statement to check whether current_key is empty before calling the encryption function. 
If no password has been set, the program now returns ERROR Password not set instead of crashing. 

I also fixed the output formatting by adding RESULT before the encrypted string.

encryption.py appears to be working as intended. 
The program can now handle PASS, ENCRYPT, DECRYPT, and QUIT commands.
For my next session, I plan to start working on driver.py.

# 10-16-2026 8:52pm - Session 6 Start
Now that both logger.py and encryption.py are working, I plan to start working on driver.py.
For this session, I plan to focus on creating the processes and setting up pipes.
I plan to look at the cpu.py and mem.py examples provided to understand how to create processes and send information between them.
I want to start by getting the driver to send a message to the logger and checking whether it gets recorded in the log file. 
After that, I plan to have the driver send PASS and ENCRYPT commands to the encryption program and read the RESULT response. 
My goal for this session is to get all three programs communicating correctly before implementing the user menu and history.

# 10-16-2026 9:44pm - Session 6 End
I created driver.py and started working on connecting the three programs together. 
I used the subprocess module and Popen to launch logger.py and encryption.py as two separate child processes.
I started by having the driver send a START message to the logger to see if it would record the message in test.log. 
After that, I tested sending PASS HELLO, ENCRYPT HELLO, and DECRYPT OIWWC to the encryption program. 
I checked test.log and saw that the logger recorded the commands and results with timestamps.
It looks like all three programs are communicating correctly. 
For my next session, I plan to implement the interactive user menu and history feature.

# 10-16-2026 11:29pm - Session 7 Start
driver.py currently uses hardcoded test values, so the user cannot interact with the program yet.
I plan to implement the interactive menu and history feature. 
I will create a while loop that continuously displays the available commands.
I also plan to create a list to store the history of strings entered by the user and the results of encryption and decryption.
My goal for this session is to get the menu and history working before connecting the user's choices to the encryption program.