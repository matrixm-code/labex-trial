#!/bin/bash

#validates the command-line argument, if directory name is not passed the print content of working directory 
if [ $# -eq 0 ]
then
	echo -e "\n\e[42m[OUTPUT]\e[0m CONTENT OF THE PRESENT  DIRECTORY \e[42m[OUTPUT]\e[0m"
	find . -maxdepth 1 | rev | cut -d '/' -f 1 | rev
else

#performs the display operation for all the input directories
	for((i=1; i<=$#; i++))
	do
		echo $var1
		 echo -e "\n\e[42m[OUTPUT]\e[0m CONTENT OF THE DIRECTORY \e[42m[OUTPUT]\e[0m"
		 
		
		 eval var=\$$i
	 	 find $var -maxdepth 1 |rev | cut -d '/' -f 1 | rev

	done

fi




