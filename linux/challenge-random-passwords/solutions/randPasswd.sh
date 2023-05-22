#!/bin/bash

echo -e "\e[44m[INPUT]\e[0m Enter the Number of Password to Generate \e[44m[INPUT]\e[0m"
read number

#gets an character from urandom and translate into 8 character value
echo -e "\e[41m[OUTPUT]\e[0m Random Generated Password is \e[41m[OUTPUT]\e[0m"
cat /dev/urandom | tr -cd 'a-zA-Z0-9~!@#$%^&*()_+}{":?><' | fold -w 8 | head -n $number



