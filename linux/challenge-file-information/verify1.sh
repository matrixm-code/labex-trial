#!/bin/zsh

cd ~/project

if [ $(bash fileInfo.sh | wc -l) -eq 4 ];then
	exit 0
else
	exit 1
fi