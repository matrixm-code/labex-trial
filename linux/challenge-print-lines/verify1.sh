#!/bin/zsh

cd ~/project
a=$(bash printLines.sh 1 2 inputFile.txt | head -1)
b=$(bash printLines.sh 1 2 inputFile.txt | tail -n 1)
if [[ $a == "is" && $b == "my" ]];then
	exit 0
else
	exit 1
fi