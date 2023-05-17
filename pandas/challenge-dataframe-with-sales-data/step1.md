# Data Cleaning

In this sub-challenge, your goal is to clean and preprocess the raw sales data. This step is crucial to ensure that the dataset is free of errors and inconsistencies, which could affect the accuracy of your analysis.

**TODO:**

1.  Create the `clean_data` function in the `data_cleaning.py`.
2.  Convert the 'Date' column to datetime using `pandas.to_datetime`.
3.  Clean the duplicate row and rows with missing values in the `DataFrame` and return the DataFrame.

## Example

Challengers can run the data_cleaning.py file to verify the correctness of the code:

```
python3 data_cleaning.py

# output:
#          Date    Product     Category  Price  Items Sold
# 0  2021-03-01  Product A  Electronics    300        10.0
# 1  2021-03-02  Product B  Electronics    150         7.0
# 2  2021-03-03  Product C         Home     60        20.0
# 3  2021-05-04  Product C      Fashion     40        15.0
# 4  2021-05-05  Product E      Fashion     80        12.0
# 5  2021-06-06  Product F         Home     90         8.0
# 6  2021-06-07  Product G  Electronics    200         6.0
# 7  2021-07-08  Product H      Fashion     50        14.0
# 8  2021-07-10  Product C         Home    100         9.0
# 9  2021-07-10  Product J  Electronics    350         4.0
# 10 2021-07-11  Product K      Fashion    120        10.0
# 11 2021-07-11  Product N  Electronics    400         5.0
# 13 2021-09-14  Product N      Fashion     60        16.0
# 14 2021-10-15  Product O         Home     70        13.0
# 15 2021-10-16  Product P  Electronics    250         7.0
# 16 2021-11-17  Product Q      Fashion    100         9.0
```
