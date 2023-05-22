#!/bin/bash

#path from the $PATH is Seperated using tr-command
file=(`echo $PATH | tr ":" "\n" `)


#checks the executable file for all the current directory
for((i=0; i<${#file[@]}; i++))
do	
	echo -e  "\n\ncurrent directory: ${file[$i]}"
	count=(`find ${file[$i]} -maxdepth 1 -executable | wc -l`)

	echo "current count:$count"
	totalCount=$(($totalCount+$count))
done
	

#prints the total count of the Executable Files
	echo -e "\n\n\e[42m[OUTPUT]\e[0m Total-Count:[$totalCount] \e[42m[OUTPUT]\e[0m"


#echo  $PATH | sed 's/[^:]//g'| tr -d '\012' | wc -c
