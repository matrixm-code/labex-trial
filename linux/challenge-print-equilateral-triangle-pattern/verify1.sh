#!/bin/zsh

cd ~/project
echo -e "4\n" | bash pattern2.sh > /tmp/output.txt
rs=$(cat /tmp/output.txt | tail -n 1 | awk '{print $4}')
if [[ $rs -eq 10 ]];then
	exit 0
else
	exit 1
fi