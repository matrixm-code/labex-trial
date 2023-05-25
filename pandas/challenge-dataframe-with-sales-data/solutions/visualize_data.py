# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from data_aggregation import aggregate_data

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
    # Total Revenue per Product
    plt.figure(figsize=(10, 6))
    plt.bar(total_revenue_per_product['Product'], total_revenue_per_product['Revenue'])
    plt.xlabel('Product')
    plt.ylabel('Revenue')
    plt.title('Total Revenue per Product')
    plt.xticks(rotation=90)
    plt.show()

    # Average Price per Category Over Time
    plt.figure(figsize=(10, 6))
    for category in df['Category'].unique():
        category_df = df[df['Category'] == category]
        plt.plot(category_df['Date'], category_df['Price'], label=category)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Average Price per Category Over Time')
    plt.legend()
    plt.show()

    # Feature Correlations
    plt.figure(figsize=(10, 6))
    correlations = df.corr(numeric_only=True)
    cax = plt.matshow(correlations, vmin=-1, vmax=1, cmap='coolwarm')
    plt.colorbar(cax)
    plt.xticks(range(len(correlations.columns)), correlations.columns, rotation=90)
    plt.yticks(range(len(correlations.columns)), correlations.columns)
    plt.title('Feature Correlations')
    plt.show()

    # Sales Distribution by Season
    plt.figure(figsize=(10, 6))
    plt.pie(season_sales['Revenue'], labels=season_sales['Season'], autopct='%1.1f%%')
    plt.title('Sales Distribution by Season')
    plt.show()


if __name__ == '__main__':
    df=pd.read_csv('ef.csv')
    df=df.loc[:,~df.columns.str.contains("^Unnamed")]
    df['Date'] = pd.to_datetime(df['Date'])
    total_revenue_per_product, avg_price_per_category, top_10_products, season_sales = aggregate_data(df)
    season_sales = df.groupby('Season')['Revenue'].sum().reset_index()
    visualize_data(df, total_revenue_per_product, avg_price_per_category, top_10_products, season_sales)
    