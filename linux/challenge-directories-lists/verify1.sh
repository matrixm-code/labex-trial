#!/bin/zsh

cd ~/project

bash dirList.sh ~/project ~/project/dir > /tmp/output.txt

rs=$(cat /tmp/output.txt | egrep "*.sh" | wc -l)
if [ $rs -eq 2 ];then
	rm /tmp/output.txt
	exit 0
else
	rm /tmp/output.txt
	exit 1
fi
