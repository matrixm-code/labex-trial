#!/bin/zsh

cd ~/project
bash longAndShort.sh > /tmp/output.txt
tail -n 1 /tmp/output.txt | grep "lp"
rs=$?
tail -n 2 /tmp/output.txt | grep "systemd-timesync"
rs1=$?
if [[ $rs -eq 0 && $rs1 -eq 0 ]];then
	exit 0
else
	exit 1
fi