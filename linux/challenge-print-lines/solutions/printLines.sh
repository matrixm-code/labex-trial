#!/bin/bash

#validating the arguments 
if [ $# -eq 3 ]
then
#validating the arg1 and arg2 to be numbers
	if [ $1 -gt 0 -a $2 -gt 0 ]	
	then
		headCount=$(($1+$2))
		head -n  $headCount $3 | tail -n $2 | cat 
		exit 0
	else
		echo -e  "\n\n\t\t\e[41m[ERROR]\e[0marguments missing!\e[41m[ERROR]\e[0m\nUsage: ./file_filter.sh start_line uptoline filename\nFor eg. ./20_file_filter.sh 5 5 <file>"
		exit 0
	fi	


else
	echo -e  "\e[41m[ERROR]\e[0m Please Pass an argument to perform an Operation \e[41m[ERROR]\e[0m"
#calling a function from " exit.sh" file
	exit 0

fi


