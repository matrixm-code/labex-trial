#!/bin/zsh
if  grep -q "plt.bar(" "/home/labex/project/data_visualization.py" ; then
    if  grep "plt.plot/|plt.legend(" "/home/labex/project/data_visualization.py" ; then
        if grep "plt.matshow/|plt.colorbar" "/home/labex/project/data_visualization.py"; then
            if grep -q "plt.pie" "/home/labex/project/data_visualization.py"; then
                if grep "plt.xlabel/|plt.ylabel/|plt.title" "/home/labex/project/data_visualization.py"; then
                    if grep -q "plt.show()" "/home/labex/project/data_visualization.py"; then
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