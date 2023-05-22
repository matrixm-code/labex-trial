# Adding Two Numbers

Write a script for addition of two numbers for real numbers also.

## Prerequisites:

- How to add real numbers in script.
- How to use piping in commands.
- Script name: `add2No.sh`.
- Work directory: `~/project`.

## Objective:

- To understand working of piping.
- To learn arithmetic operations in shell script.

## Requirements:

- Ask user to enter two numbers.
- User can enter real numbers also.
- Use `bc` command and piping to do.

## Sample Execution / Output:

```bash
labex:project/ $ bash add2No.sh
[INPUT] Enter the value of Number1      [INPUT]
12
[INPUT] Enter the value of Number2      [INPUT]
13
[INPUT] Enter the method to be used in Addition operation       [INPUT]
                1)method 1 uses expr command to add two numbers
                2)method 2 uses bc (floating point is accepted) command to add two numbers
                3)method 3 uses (( )) command to add two numbers
1


[OUTPUT]OPERATION PERFORMED[OUTPUT]
12+13 = 25
```
