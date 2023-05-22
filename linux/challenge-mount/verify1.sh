#!/bin/zsh

cd ~/project

bash mount.sh /dev/vda3 > /tmp/output.txt

cat /tmp/output.txt | grep "used"
rs=$?
cat /tmp/output.txt | grep "free"
rs1=$?
if [[ $rs -eq 0 && $rs1 -eq 0 ]];then
	exit 0
else
	exit 1
fi