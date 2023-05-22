#!/bin/bash



#prompt the user to get the value and store it in the variable inputNumber

echo -e "\t\t\t**********\tEnter the value that is need to be reversed\t**********"
read  inputNumber

dummyInput=$inputNumber
reverseFinalResult=0


declare -a remainder=()


#validate whether the given input is number else throw an error
if [ $inputNumber -gt 0 ]
then
	while [ $dummyInput -gt 0 ]
	do 

		remainder=$(($dummyInput%10))	#captures the remainder of the input for each iteration
		reverseFinalResult=$(($reverseFinalResult*10+$remainder))	#addeds tens value before adding remainder in th Reverseresult
		dummyInput=$(($dummyInput/10))	#removes the last number in  the input value  
			
	done 

 	echo "[OUTPUT]Reversed value of $inputNumber is : $reverseFinalResult[OUTPUT]"


else
	echo -e "\t\t\t**********\t\tplease give a valid input to perform an operation\t\t**********\t\t\t"

fi

