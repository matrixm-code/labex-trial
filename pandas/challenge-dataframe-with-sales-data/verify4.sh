#!/bin/zsh
if  grep -q "plt.bar(" "/home/labex/project/data_visualization.py" ; then
    if  grep -q "plt.plot" "/home/labex/project/data_visualization.py"; then
        if grep -q "plt.matshow" "/home/labex/project/data_visualization.py"; then
            if grep -q "plt.pie" "/home/labex/project/data_visualization.py"; then
                if grep -q "plt.xlabel" "/home/labex/project/data_visualization.py" && grep -q "plt.ylabel" "/home/labex/project/data_visualization.py" && grep -q "plt.title" "/home/labex/project/data_visualization.py"; then
                    if grep -q "plt.show()" "/home/labex/project/data_visualization.py"; then
                        
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