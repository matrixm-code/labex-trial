# Print Lines

Write script to print contents of file from given line number to next given number of lines.

## Prerequisites:

- Piping in shell.
- `head` and `tail` commands.
- Script name: `printLines.sh`.
- Work directory: `~/project`.

## Objective:

- To learn about file filter commands.

## Requirements:

- Pass three command-line arguments:
  - 1- starting line number
  - 2- number of lines
  - 3- filename
- Script will print n lines from given starting line.

## Sample Execution / Output:

```bash
labex:project/ $ bash printLines.sh 3 5 inputFile.txt
name
and
i
like
to
```

```bash
labex:project/ $ bash printLines.sh 10 2 inputFile.txt
arch
linux
```
