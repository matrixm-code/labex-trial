#!/bin/bash

#pushes all the user name into var
var=(`cat /etc/passwd|cut -d ':' -f 1`)
present=0

#prompts the user for the username
echo -e "\n\t\e[44m[INPUT]\e[0m Enter the username \e[44m[INPUT]\e[0m"
read userName


#Displays the username if present else displays if not present
function display()
{

	if [ $1 -eq 0 ]
	then
		echo -e "\n\t\e[42m[OUTPUT]\e[0m USER $2 IS NOT PRESENT \e[42m[OUTPUT]\e[0m\n"
	else
		echo -e "\n\t\e[42m[OUTPUT]\e[0m USER $2 IS PRESENT \e[42m[OUTPUT]\e[0m\n"
	fi


}

#validates the username presence in the system
for((i=0; i<${#var[@]}; i++))
do
	if [ ${var[i]}	== $userName ]
	then
		present=1
		display $present $userName
	fi
done


#if the username is not present then calls the display function
if [ $present -eq 0 ]
then
	display $present $userName
fi

exit 0




