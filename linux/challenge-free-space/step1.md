# Free Space

Read a `n` and display the names of any file-system which have less than `n%` free space available.

## Prerequisites:

- Must know commands `df`, `tr` and `cut`.
- Use of arrays and loops.
- Script name: `freeSpace.sh`.
- Work directory: `~/project`.

## Objective:

- Learn more about mounting, file-systems and device files.

## Requirements:

- When you run the script show all file-system present in system.
- Then print file-systems that have only `n%` memory remaining.

## Sample Execution / Output:

```bash
labex:project/ $ bash freeSpace.sh
[INPUT] Enter the usage [INPUT]
12
file system "/dev/mapper/docker-252:3-1311728-cf1bc296802376b110e1ac0a19ed3ad263fc81be8ff146ddfbd4acc246b61682"  has "62%" of freespace and used space of 38%
file system "/dev/vda3"  has "54%" of freespace and used space of 46%
```

```bash
labex:project/ $ bash freeSpace.sh
[INPUT] Enter the usage [INPUT]
60
No file System has usage of 40% of freeSpace
```
