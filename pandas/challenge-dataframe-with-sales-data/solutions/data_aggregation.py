import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Sub-challenge 3: Data Aggregation
def aggregate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, str]:
    """
    Aggregate the data to answer specific questions or derive insights about the dataset.
    
    :param df: The input DataFrame containing cleaned and engineered sales data.
    :return: A tuple containing the aggregated data results.
    """

    # TODO: implement this function here.
    # Note: Do not change the existing code.
    total_revenue_per_product = df.groupby('Product')['Revenue'].sum().reset_index()
    avg_price_per_category = df.groupby('Category')['Price'].mean().reset_index()
    top_10_products = total_revenue_per_product.nlargest(10, 'Revenue')
    season_sales = df.groupby('Season')['Revenue'].sum().reset_index()
    highest_sales_season = season_sales.loc[season_sales['Revenue'].idxmax(), 'Season']

    return total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season

if __name__ == '__main__':
    df=pd.read_csv('ef.csv')
    total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season = aggregate_data(df)
    print(total_revenue_per_product)
    print(avg_price_per_category)
    print(top_10_products)
    print(highest_sales_season)
    