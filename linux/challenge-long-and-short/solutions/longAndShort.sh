#!/bin/bash

#captures all the username from the system in an array nameArray
nameArray=(`cat /etc/passwd | cut -d ':' -f 1`)
countOfArray=${#nameArray[@]}


#performs assending order operation where smallest number comes first and largest comes last
for((i=0; i<$countOfArray; i++))
do
	for((j=$(($i+1)); j<$countOfArray; j++))
	do
		if [ ${#nameArray[i]} -gt ${#nameArray[j]} ]
		then
			 temp=${nameArray[i]}
		nameArray[$i]=${nameArray[j]}
		nameArray[$j]=$temp
		fi
		
	done

done

echo -e "\n\n\e[42m[OUTPUT]\e[0m Largest and Shortest UserName \e[42m[OUTPUT]\e[0m"
echo "Largest Username is ${nameArray[$countOfArray-1]}"
echo "Smallest Username is ${nameArray[0]}"



