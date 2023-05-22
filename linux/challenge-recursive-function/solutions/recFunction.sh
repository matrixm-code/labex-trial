#!/bin/bash

function display()
{
#print the first value of the arguments
	echo $1

#get content of the arguments 
gotArray=("$@")

#remove 1 argument and push to another array
for((i=1; i<=${#gotArray[@]}; i++ ))
do
	array[i-1]=${gotArray[i]}
done


#validate whether $1 has value if not exit
if [ $1 ]
then
display ${array[@]}
fi 


	
}

if [ $# -gt 0 ]
then
#call the dislay function from the main function
	echo -e "\e[42m[OUTPUT]\e[0m Arguments passed are \e[42m[OUTPUT]\e[0m"
	display $@
else
	echo -e "\e[41m[ERROR]\e[0m Please pass an argument to perform the operation \e[41m[ERROR]\e[0m"	
fi





