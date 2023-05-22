# Mount

Write a script to determine whether a given file system or mount point is mounted.

## Prerequisites:

- Must know commands `df`, `tr`, and `cut`.
- Use of arrays and loops.
- Script name: `mount.sh`.
- Work directory: `~/project`.

## Objective:

- Learn more about mounting, file-systems, and device files.

## Requirements:

- Check if the given file system is mounted or not.
- If it's mounted, print the free space available in it.
- Otherwise, print an error message.

## Sample Execution / Output:

```bash
labex:project/ $ bash mount.sh /dev/vda3
 Filesystem /dev/vda3 is 46% used with 21367676 KB free.
```
