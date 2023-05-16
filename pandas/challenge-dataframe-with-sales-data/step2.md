# Feature Engineering

In this sub-challenge, you will create new features from the existing data to enhance your analysis. Feature engineering can help you uncover hidden patterns and relationships within the data, which can lead to more accurate predictions and insights.

**TODO:**

<!-- 1. Create a new feature 'Revenue' by multiplying 'Price' and 'Items Sold'.
2. Extract 'Year', 'Month', and 'Day' columns from the 'Date' column using the Pandas `pandas.dt`.
3. Create a new feature 'Price Category' based on the 'Price' column (e.g., low, medium, high) in the function `price_category`.
4. Create a new feature 'Season' based on the 'Month' column in the function `season`. -->

1.  Create the `engineer_features` function in the `engineer_features.py`.
2.  Create a new feature `Revenue` by multiplying `Price` and `Items Sold`.
3.  Use the the Pandas `pandas.dt` to extract 'Year', 'Month', and 'Day' columns from the `Date` column.
4.  Create a new feature `Price Category` based on the `Price` column (e.g., low, medium, high) by writing `price_category` function.
5.  Create a new feature `Season` based on the `Month` column by writing `season` function.

## Example

Challengers can run the feature_engineering.py file to verify the correctness of the code:

```
python3 data_cleaning.py
python3 feature_engineering.py

#output:
          Date    Product      Category    Price   Items Sold    Revenue    Year    Month   Day     Price Category    Season
0   2021-03-01  Product A   Electronics     300          10.0     3000.0    2021        3     1               High    Spring
1   2021-03-02  Product B   Electronics     150           7.0     1050.0    2021        3     2             Medium    Spring
2   2021-03-03  Product C   Home             60          20.0     1200.0    2021        3     3                Low    Spring
3   2021-05-04  Product C   Fashion          40          15.0      600.0    2021        5     4                Low    Spring
4   2021-05-05  Product E   Fashion          80          12.0      960.0    2021        5     5             Medium    Spring
5   2021-06-06  Product F   Home             90           8.0      720.0    2021        6     6             Medium    Summer
6   2021-06-07  Product G   Electronics     200           6.0     1200.0    2021        6     7               High    Summer
7   2021-07-08  Product H   Fashion          50          14.0      700.0    2021        7     8                Low    Summer
8   2021-07-10  Product C   Home            100           9.0      900.0    2021        7    10             Medium    Summer
9   2021-07-10  Product J   Electronics     350           4.0     1400.0    2021        7    10               High    Summer
10  2021-07-11  Product K   Fashion         120          10.0     1200.0    2021        7    11             Medium    Summer
11  2021-07-11  Product N   Electronics     400           5.0     2000.0    2021        7    11               High    Summer
13  2021-09-14  Product N   Fashion          60          16.0      960.0    2021        9    14                Low      Fall
14  2021-10-15  Product O   Home             70          13.0      910.0    2021       10    15             Medium      Fall
15  2021-10-16  Product P   Electronics     250           7.0     1750.0    2021       10    16               High      Fall
16  2021-11-17  Product Q   Fashion         100           9.0      900.0    2021       11    17             Medium      Fall
```
