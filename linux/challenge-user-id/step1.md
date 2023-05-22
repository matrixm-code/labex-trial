# User Id

Count the number of users with user IDs between 500 and 10000 on the system.

## Prerequisites:

- Must know `df`, `cut` & `tr` commands.
- Loops and arrays.
- Script name: `userId.sh`.
- Work directory: `~/project`.

## Objective:

- Learn about `etc` configuration files.

## Requirements:

- Fetch user-ids from the `/etc/passwd` file.
- Display only usernames between the range.
- User can change the range using command-line arguments.

## Sample Execution / Output:

```bash
labex:project/ $ bash userId.sh 

[OUTPUT] UID AND USERNAEM [OUTPUT]
5000 :labex
999 :mongodb
[OUTPUT]Total count of User-id Between 500 to 10000 is "2" [OUTPUT]
```

