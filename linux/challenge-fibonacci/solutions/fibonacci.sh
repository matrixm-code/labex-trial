#!/bin/bash

#read the number from the user and perform Fibonacci series operation
echo "[INPUT]Enter the value of N[INPUT]"
read n

if [ $n -gt 0 ]
then

	declare -a array=( 0 1 )


	echo "[OUTPUT]Fibonacci Series of Given Number $n is [OUTPUT]"
	echo -ne "${array[0]}\t";
	echo -ne "${array[1]}\t";


	for((i=2;i<=n;i++))
	do
		
		array[i]=$((${array[i-2]}+${array[i-1]}))
		if [ ${array[i]} -lt $n ]
		then
			count=$i
			echo -ne  "${array[i]}\t"
		
		else
			echo -e "\n\n\nlargest of given fibonacci series is:${array[$count]}\n\n"			
			exit 0
		fi
	done

else
	echo "[Error]Invalid Input[Error]"
fi




