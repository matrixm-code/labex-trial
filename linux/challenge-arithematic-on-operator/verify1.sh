#!/bin/zsh

echo -e "123+\n" | bash ~/project/arithematicOnOperator.sh 2> /dev/null | tail -n 1 | grep -q "6"
