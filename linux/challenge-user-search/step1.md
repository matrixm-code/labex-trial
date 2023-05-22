# User Search

Write a script to search a user present in your system.

## Prerequisites:
- Must know `df`, `cut` & `tr` commands.
- Loops and arrays.
- Script name: `userSearch.sh`.
- Work directory: `~/project`.

## Objective:
- Learn about `etc` configuration files.

## Requirements:
- Fetch user-names from the first field in `/etc/passwd` file.
- Search given name in the list.

### Sample Execution / Output:

```bash
labex:project/ $ bash userSearch.sh 

        [INPUT] Enter the username [INPUT]
labex

        [OUTPUT] USER labex IS PRESENT [OUTPUT]
```

```bash
labex:project/ $ bash userSearch.sh

        [INPUT] Enter the username [INPUT]
123

        [OUTPUT] USER 123 IS NOT PRESENT [OUTPUT]
```

