#!/bin/bash

#validates the arguments
if [ $# -gt 2 ] 
then
	declare -a inputValue=("$@")
	echo "inputcount : ${#inputValue[@]}"
	echo "content of inputValue ${inputValue[@]}"
#compares the first value with n-numbers of values till it reaches its proper index
	for((j=0; j<=${#inputValue[@]}; j++))
	do
		for((i=$(($j+1)); i<${#inputValue[@]}; i++))
		do

			if [  ${inputValue[j]} -gt  ${inputValue[i]} ] 
			then
				temp=${inputValue[$j]}
				inputValue[$j]=${inputValue[$i]}
				inputValue[$i]=$temp
			fi 
		done

	done
#prompts the user for user-option
	echo  -e "\e[44m[Input]\e[0m Enter your choice \e[44m[Input]\e[0m"
	echo -e "1.Ascending \n2.Descending"
	read choice

#validates the user-choices
	if [ $choice -eq 1 ]
	then
		echo -e "\e[42m[OUTPUT]\e[0m Ascending Order \e[42m[OUTPUT]\e[0m"
		echo ${inputValue[@]}
		exit 0
	elif [ $choice -eq 2 ]
	then 
		declare -a reverse=()
		echo -e "\e[42m[OUTPUT]\e[0m Descending Order \e[42m[OUTPUT]\e[0m"
		for((i="${#inputValue[@]}"; i>=0; i--))
		do
			reverse+=(${inputValue[i]})
		done
		 echo ${reverse[@]}
		exit 0
	else
		echo -e "\e[41m[ERROR]\e[0m Invalid Choice \e[41m[ERROR]\e[0m"
		exit 0
	fi


else
	echo  -ne  "\e[41m[ERROR]\e[0m Please pass more than one argument to perform sort operation \e[41m[ERROR]\e[0m" 
	exit 0

fi




