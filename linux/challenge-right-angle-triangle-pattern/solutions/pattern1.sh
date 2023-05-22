#!/bin/bash

#prompt the user to enter the value of N and store it in the variable
echo "[INPUT]Enter the value of N[INPUT]"
read inputN

if [ $inputN -gt 0 ]
then
	echo "[OUTPUT]Expected Pattern is Shown Below[OUTPUT]"
	for ((row=1; row<=inputN; row++))
	do
	for ((col=1; col<=row; col++))
	do
		echo -en   "$col\t"
	done
		echo " "
	done
else
	echo "[ERROR]Invalid Input[ERROR]"
fi

