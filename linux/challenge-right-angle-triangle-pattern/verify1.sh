#!/bin/zsh

a=$(echo -e "3\n" | bash ~/project/pattern1.sh | tail -n 1 | awk '{print $1}')
b=$(echo -e "3\n" | bash ~/project/pattern1.sh | tail -n 1 | awk '{print $2}')
c=$(echo -e "3\n" | bash ~/project/pattern1.sh | tail -n 1 | awk '{print $3}')
if [[ $a -eq 1 && $b -eq 2 && $c -eq 3 ]]
then
	exit 0
else
	exit 1
fi