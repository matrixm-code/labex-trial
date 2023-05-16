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
python3 feature_engineering.py
```

The DataFrame processing result is as follows:

![feature_engineering_result_image](assets/feature_engineering_result.png)
