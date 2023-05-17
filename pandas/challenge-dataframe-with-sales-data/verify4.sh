#!/bin/zsh
if  grep -q "bar" "/home/labex/project/data_visualization.py" ; then
    if  grep -q "plot" "/home/labex/project/data_visualization.py"; then
        if grep -q "matshow" "/home/labex/project/data_visualization.py"; then
            if grep -q "pie" "/home/labex/project/data_visualization.py"; then
                if grep -q "xlabel" "/home/labex/project/data_visualization.py" && grep -q "ylabel" "/home/labex/project/data_visualization.py" && grep -q "title" "/home/labex/project/data_visualization.py"; then
                    if grep -q ".show()" "/home/labex/project/data_visualization.py"; then
                        cd /tmp && python3 test_data_visualization.py
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
    else
        exit 1;
    fi
else
    exit 1;
fi