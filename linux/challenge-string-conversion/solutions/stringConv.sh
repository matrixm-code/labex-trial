#!/bin/bash

#validates the user to pass an arguments
if [ $# -eq 1 ]
then

#reads the users option
	echo -e "\n\e[44m[INPUT]\e[0m\tPlease Select an option\t\e[44m[INPUT]\e[0m\n\t1.TO_UPPER_CASE\n\t2.to_lower_case"
	read userOption

#validates the user option using case statements
case $userOption in


1)	cat $1|tr [:lower:] [:upper:] > new.txt 
	sudo mv new.txt $1 
	echo -e "\e[42m[OUTPUT]\e[0m content of Input File AFTER OPERATION \e[42m[OUTPUT]\e[0m\n`cat $1`"
	exit 0 ;;

2)	cat $1|tr [:upper:] [:lower:] > new.txt 
	sudo mv new.txt $1 
	echo -e "\e[42m[OUTPUT]\e[0m content of Input File AFTER OPERATION \e[42m[OUTPUT]\e[0m\n`cat $1`"
	exit 0 ;;
esac

else
	echo -e	"\e[41m[ERROR]\e[0m Please pass an input-file to Perform an operation \e[41m[ERROR]\e[0m"
	exit 0
fi




