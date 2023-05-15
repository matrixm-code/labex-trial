# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from data_aggregation import aggregate_data

df=pd.read_csv('ef.csv')
total_revenue_per_product, avg_price_per_category, top_10_products, season_sales = aggregate_data(df)

# Sub-challenge 4: Data Visualization
def visualize_data(df: pd.DataFrame, total_revenue_per_product: pd.DataFrame, avg_price_per_category: pd.DataFrame, top_10_products: pd.DataFrame, 
                    season_sales: pd.DataFrame) -> None:
    """
    Create visualizations to help better understand the dataset and communicate findings.
    
    :param df: The input DataFrame containing cleaned and engineered sales data.
    :param total_revenue_per_product: DataFrame containing total revenue per product.
    :param avg_price_per_category: DataFrame containing average price per category.
    :param season_sales: DataFrame containing sales by season.
    :return: None
    """
    
    # TODO: implement this function here.
    # Note: Do not change the existing code.


if __name__ == '__main__':
    season_sales = df.groupby('Season')['Revenue'].sum().reset_index()
    visualize_data(df, total_revenue_per_product, avg_price_per_category, top_10_products, season_sales)