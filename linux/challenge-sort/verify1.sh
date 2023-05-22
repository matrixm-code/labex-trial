#!/bin/zsh

rs=$(echo -e "1\n" | bash ~/project/sort.sh 1 3 2 | tail -n 1)
rs1=$(echo -e "2\n" | bash ~/project/sort.sh 1 3 2 | tail -n 1)
if [[ $rs == "1 2 3" && $rs1 == "3 2 1" ]]
then
	exit 0
else
	exit 1
fi
