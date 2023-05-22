# Path Count

The objective of this script is to display the number of executable files in each directory listed in the `$PATH` environmental variable.

## Prerequisites:

- Must know bash environmental variables.
- Working of `tr` command.
- Loops and arrays.
- Checking permission of files in script.
- Script name: `pathCount.sh`.
- Work directory: `~/project`.

## Objective:

- Learn significance of `PATH` variable.

## Requirements:

- Fetch each directories from `PATH` variable.
- Use `-x` option in the `if` condition to check executable permission.
- Print directory and number of executable files one-by-one.
- Print the total number of executable files at last.
- Count only files have executable permission.
- Verify path is present every time.

### Sample Execution / Output:

```bash
labex:project/ $ bash pathCount.sh


current directory: /usr/lib/jvm/java-11-openjdk-amd64/bin
current count:34


current directory: /usr/lib/jvm/java-11-openjdk-amd64/bin
current count:34


current directory: /usr/lib/code-server/lib/vscode/bin/remote-cli
current count:2


current directory: /usr/lib/jvm/java-11-openjdk-amd64/bin
current count:34


current directory: /usr/lib/jvm/java-11-openjdk-amd64/bin
current count:34


current directory: /usr/local/sbin
current count:2


current directory: /usr/local/bin
current count:13


current directory: /usr/sbin
current count:267


current directory: /usr/bin
current count:1511


current directory: /sbin
current count:1


current directory: /bin
current count:1


current directory: /home/labex/.local/bin
current count:61


current directory: /usr/local/go/bin
current count:3


current directory: /home/labex/golang/bin
current count:10


current directory: /usr/share/maven/bin
current count:4


current directory: /usr/local/bin
current count:13


current directory: /usr/sbin/nodejs/bin
current count:4


current directory: /usr/sbin/yarn/bin
current count:6


current directory: /home/labex/.local/bin
current count:61


current directory: /usr/local/go/bin
current count:3


current directory: /home/labex/golang/bin
current count:10


current directory: /usr/share/maven/bin
current count:4


current directory: /usr/local/bin
current count:13


current directory: /usr/sbin/nodejs/bin
current count:4


current directory: /usr/sbin/yarn/bin
current count:6


[OUTPUT] Total-Count:[2135] [OUTPUT]
```
