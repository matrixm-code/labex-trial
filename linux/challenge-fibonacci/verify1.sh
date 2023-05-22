#!/bin/zsh

cd ~/project

echo -e "5\n" | bash fibonacci.sh > /tmp/output.txt

rs=$(cat /tmp/output.txt | grep "3" | wc -l)

if [ $rs -eq 2 ];then
	exit 0
else
	exit 1
fi