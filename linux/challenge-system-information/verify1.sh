#!/bin/zsh

USER=$(whoami)
echo -e "1\n" | bash ~/project/sysInfo.sh | grep -q $USER