#!/bin/zsh

cd ~/project
len=$(echo -e "3\n" | bash chessBoard.sh 2> /dev/null | tail -n 4 | wc -l) 
if [ $len -eq 3 ];then
	exit 0
else
	exit 1
fi
