#!/bin/zsh

cd ~/project
a=$(echo $PATH | sed 's/:/\n/g' | wc -l)
b=$(bash pathCount.sh 2> /dev/null | grep "\/" | wc -l)
if [[ $a -eq $b ]];then
	exit 0
else
	exit 1
fi