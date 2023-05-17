# Data Aggregation

In this sub-challenge, you will aggregate the data to answer specific questions or derive insights about the dataset. Data aggregation involves grouping and summarizing data to reveal patterns or trends.

**TODO:**

1.  Create the `aggregate_data` function in the `aggregate_data.py`.
2.  Calculate the total revenue for each product.
3.  Calculate the average price per category.
4.  Find the top 10 products with the highest revenue.
5.  Identify the season with the highest sales.

## Example

Challengers can run the data_aggregation.py file to verify the correctness of the code:

```
python3 data_cleaning.py
python3 feature_engineering.py
python3 data_aggregation.py

# output:
# (      Product  Revenue
#  0   Product A   3000.0
#  1   Product B   1050.0
#  2   Product C   2700.0
#  3   Product E    960.0
#  4   Product F    720.0
#  5   Product G   1200.0
#  6   Product H    700.0
#  7   Product J   1400.0
#  8   Product K   1200.0
#  9   Product N   2960.0
#  10  Product O    910.0
#  11  Product P   1750.0
#  12  Product Q    900.0,
#        Category  Price
#  0  Electronics    275
#  1      Fashion     75
#  2         Home     80,
#        Product  Revenue
#  0   Product A   3000.0
#  9   Product N   2960.0
#  2   Product C   2700.0
#  11  Product P   1750.0
#  7   Product J   1400.0
#  5   Product G   1200.0
#  8   Product K   1200.0
#  1   Product B   1050.0
#  3   Product E    960.0
#  10  Product O    910.0,
#  'Summer')
```
