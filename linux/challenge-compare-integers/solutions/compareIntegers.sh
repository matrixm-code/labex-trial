#!/bin/bash



if [ $# -gt "0" ] #validates whether the argument is passed as an command line argument
then 	

	declare -a array=( "$@" ) #argument values are captured and pushed into an array
	largest=${array[0]} #first value is initalized as an largest number initally

#compare the initalized largest value with n-integer values	
	for((i=1; i<${#array[@]} ;i++))
	do
	
		if [ $largest -lt ${array[i]} ]
		then
			largest=${array[i]}
		elif [ $largest -gt ${array[i]} ]
		then
			largest=$largest
		fi
	done 



#print the final largest value among the given n-integers after comparing
   	clear
	echo -e "Largest number in n-integer value is:\t$largest"
	
else
#print error message saying argument are not passed 
	clear
	echo -e "\n\n\n\n\t\t\t\t********************\tTry again with Passing an Argument\t****************************\t\t\t"
	echo -e "\t\t\t********************\t\t\tThank you\t\t*************************\t\t\t\t\n\n\n\n"
	exit
fi




