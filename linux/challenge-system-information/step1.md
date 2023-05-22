# System Information

Write a script to print the following system information:

1. Currently logged users
2. Your shell directory
3. Home directory
4. OS name & version
5. Current working directory
6. Number of users logged in
7. Show all available shells in your system
8. Hard disk information
9. CPU information
10. Memory information
11. File system information
12. Currently running process

## Prerequisites:

- Knowledge about user commands `w`, `who`, `whoami`.
- Bash environmental variables.
- `/proc` file-system.
- Other system info commands like `df`, `du`, `uname`, `ps`.
- Script name: `sysInfo.sh`.
- Work directory: `~/project`.

## Objective:

- To learn system information commands.

## Requirements:

- Provide a menu for the user about what information he wants to check.
- Using switch case, display output for the selected option.

## Sample Execution / Output:

```bash
labex:project/ $ bash sysInfo.sh
[INPUT]Select the Option below to Display the Information[INPUT]

                                1)Currently Logged User

                                2)Shell Directory

                                3)Home Directory

                                4)OS name And OS version

                                5)Current Working Directory

                                6)Number Of users Logged-in

                                7)Available Shells in System

                                8)Hard disk Information

                                9)CPU Information

                                10)Memory Information

                                11)File-Systm Information

                                12)Currently running process(uid)

1
        [OUTPUT]Currently Logged User[OUTPUT]
        labex
```
