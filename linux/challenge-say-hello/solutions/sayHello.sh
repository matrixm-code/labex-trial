#!/bin/bash

hour=(`date +%H`)
day=(`date +%A`)
date=(`date +%d`)
month=(`date +%B`)
time=(`date +%T`)

#validates the hour
if [ $hour -ge 5 -a $hour -lt 12 ]
then
	greeting="Good Morning"
elif [ $hour -ge 12 -a $hour -lt 13 ]
then
	greeting="Good Noon"

elif [ $hour -gt 13 -a $hour -lt 17 ]
then
	greeting="Good Afternoon"
elif [ $hour -gt 17 -a $hour -lt 21 ]
then
	greeting="Good Evening"
elif [ $hour -gt 21 -a $hour -lt 5 ]
then
	greeting="Good night"
fi

clear
echo -e  "\t\t\t $greeting  `whoami`,Have a nice day!!"
echo -e  "\t\t\tThis is $day $date in $month ($time) "
echo -e "\n\n\n "




