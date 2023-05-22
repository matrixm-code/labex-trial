#!/bin/zsh

cd ~/project
echo -e "1\n" | bash freeSpace.sh > /tmp/output.txt
if [ $(cat /tmp/output.txt | wc -l) -eq 3 ];then
	exit 0
else
	exit 1
fi