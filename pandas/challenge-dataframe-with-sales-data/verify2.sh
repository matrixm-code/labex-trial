#!/bin/zsh
if  grep -q "df['Date'].dt.year" "/home/labex/project/feature_engineering.py" ; then
    if grep -q "df['Date'].dt.month" "/home/labex/project/feature_engineering.py"; then
        if grep -q "df['Date'].dt.day'" "/home/labex/project/feature_engineering.py"; then
            cd /tmp && python3 test_feature_engineering.py
        else
            exit 1
        fi
    else
        exit 1
    fi
else
    exit 1
fi