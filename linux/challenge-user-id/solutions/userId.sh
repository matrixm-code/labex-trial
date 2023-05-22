#!/bin/bash

arrayName=(`cat /etc/passwd | cut -d ':' -f 1`)
arrayUid=(`cat /etc/passwd | cut -d ':' -f 3`)
count=0


#This function searchs for the range of uid in arrayUid and prints the username using the index
function searchDisplay()
{

echo -e "\n\e[42m[OUTPUT]\e[0m UID AND USERNAEM \e[42m[OUTPUT]\e[0m"
	for((i=0; i<${#arrayUid[@]}; i++))
	do
		if [ ${arrayUid[i]} -gt $1 -a ${arrayUid[i]} -lt $2 ]
		then
			count=$((count+1))
			echo "${arrayUid[i]} :${arrayName[i]}"
		fi
	done

echo -e "\e[42m[OUTPUT]\e[0mTotal count of User-id Between $1 to $2 is \"$count\" \e[42m[OUTPUT]\e[0m"
exit 0
}



#validates the command line arguments 
if [ $# -eq 0 ] 
then
	searchDisplay 500 10000
elif [ $# -eq 2 ]
then 	
	searchDisplay $1 $2

else
	echo -e "\n\n\e[41m[ERROR]\e[0m PLEASE PASS AN ARGUMENT TO PERFORM THE OPERATION \e[41m[ERROR]\e[0m"
	exit 0
fi




