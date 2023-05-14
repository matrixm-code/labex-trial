#!/bin/zsh
if  grep -q ".dt.year" "/home/labex/project/feature_engineering.py" ; then
    if grep -q ".dt.month" "/home/labex/project/feature_engineering.py"; then
        if grep -q ".dt.day" "/home/labex/project/feature_engineering.py"; then
            if grep -q ".apply(price_category)" "/home/labex/project/feature_engineering.py" && grep -q ".apply(season)" "/home/labex/project/feature_engineering.py"; then
                cd /tmp && python3 test_feature_engineering.py
            else
                exit 1;
            fi
        else
            exit 1;
        fi
    else
        exit 1;
    fi
else
    exit 1;
fi