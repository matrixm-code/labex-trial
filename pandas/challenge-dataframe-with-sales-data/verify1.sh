#!/bin/zsh
if  grep -q "df.dropna()" "/home/labex/project/data_cleaning.py" ; then
    if grep -q ".reset_index(" "/home/labex/project/data_cleaning.py"; then
        if grep -q "pd.to_datetime(df['Date'])" "/home/labex/project/data_cleaning.py"; then
            if grep -q "df.drop_duplicates(" "/home/labex/project/data_cleaning.py"; then
                cd /tmp && python3 test_data_cleaning.py
            else
                echo 'No drop_duplicates() detected';
            fi
        else
            echo 'No to_datetime() detected';
        fi
    else
        echo 'No reset_index() detected';
    fi 
else
    exit 1;
fi
