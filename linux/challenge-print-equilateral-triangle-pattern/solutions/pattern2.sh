#!/bin/bash

#prompt the user to get the value of N and store it in the variable
echo "[INPUT]Enter  the value of N[INPUT]"
read inputN


if [ $inputN -gt 0 ]
then
	count=1
	echo "[OUTPUT]The Patter is Executed as shown below[OUTPUT]"
	for(( row=1; row<=$inputN; row++ ))
	do
	for(( col=1; col<=row; col++ ))
	do
		echo -ne "$count\t"
		count=$(($count+1))
	done
		echo " "
	done
else
	echo "[ERROR]Invalid Input[ERROR]"
fi

