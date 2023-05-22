#!/bin/zsh

echo -e "1234\n" | bash ~/project/reverse.sh | grep -q "4321"
