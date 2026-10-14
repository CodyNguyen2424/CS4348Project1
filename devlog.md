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
