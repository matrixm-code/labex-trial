#!/bin/zsh

echo -e "1\n" | bash ~/project/stringConv.sh /tmp/input_file.txt | grep "THIS"
rs=$?
echo -e "2\n" | bash ~/project/stringConv.sh /tmp/input_file.txt | grep "this"
rs1=$?
if [[ $rs -eq 0 && $rs1 -eq 0 ]]
then
	exit 0
else
	exit 1
fi
