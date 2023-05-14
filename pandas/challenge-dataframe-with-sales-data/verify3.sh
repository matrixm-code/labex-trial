#!/bin/zsh
if  grep -q ".sum()" "/home/labex/project/data_aggregation.py" ; then
    if grep -q ".mean()" "/home/labex/project/data_aggregation.py"; then
        if grep -q ".nlargest(10" "/home/labex/project/data_aggregation.py"; then
            if grep -q ".loc" "/home/labex/project/data_aggregation.py"; then
                cd /tmp && python3 test_data_aggregation.py
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