#!/bin/zsh

cd ~/project

bash compareIntegers.sh 1 2 3 4 > output.txt

cat output.txt | grep -q "4"
if [ $? -eq 0 ];then
	rm output.txt
	exit 0
else
	rm output.txt
	exit 1
fi

