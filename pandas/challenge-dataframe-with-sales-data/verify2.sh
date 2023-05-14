#!/bin/zsh
if  grep 'df['Date'].dt.year\|df['Date'].dt.month\|df['Date'].dt.day' '/home/labex/project/feature_engineering.py' ; then
    cd /tmp && python3 test_feature_engineering.py
else
    exit 1
fi