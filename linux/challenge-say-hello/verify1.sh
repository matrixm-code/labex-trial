#!/bin/zsh

who=$(whoami)
bash ~/project/sayHello.sh | grep -q $who