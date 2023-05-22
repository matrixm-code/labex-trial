#!/bin/zsh

echo -e "labex\n" | bash ~/project/userSearch.sh | grep -iq "is"
rs=$?
echo -e "labex123\n" | bash ~/project/userSearch.sh | grep -iq "not"
rs1=$?
if [[ $rs -eq 0 && $rs1 -eq 0 ]]
then
	exit 0
else 
	exit 1
fi