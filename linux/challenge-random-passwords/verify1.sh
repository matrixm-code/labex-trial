#!/bin/zsh

cd ~/project
echo -e "2\n" | bash randPasswd.sh | tail -n 2 > /tmp/output.txt
a=$(head -1 /tmp/output.txt)
b=$(tail -n 1 /tmp/output.txt)
if [[ ${#a} -eq 8 && ${#b} -eq 8 ]];then
	exit 0
else
	exit 1
fi