#!/bin/zsh

cd ~/project
bash recFunction.sh 12 a bb | grep -q "12$"
rs=$?
bash recFunction.sh 12 a bb | grep -q "a$"
rs1=$?
bash recFunction.sh 12 a bb | grep -q "bb$"
rs2=$?
if [[ $rs -eq 0 && $rs1 -eq 0 && $rs2 -eq 0 ]];then
	exit 0
else
	exit 1
fi
