import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Load sample data
data = {'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05',
                 '2021-03-06', '2021-03-07', '2021-03-08', '2021-03-09', '2021-03-10',
                 '2021-03-11', '2021-03-12', '2021-03-13', '2021-03-14', '2021-03-15',
                 '2021-03-16', '2021-03-17', '2021-03-18', '2021-03-19', '2021-03-20'],
        'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E',
                    'Product F', 'Product G', 'Product H', 'Product I', 'Product J',
                    'Product K', 'Product L', 'Product M', 'Product N', 'Product O',
                    'Product P', 'Product Q', 'Product R', 'Product S', 'Product T'],
        'Category': ['Electronics', 'Electronics', 'Home', 'Fashion', 'Fashion',
                     'Home', 'Electronics', 'Fashion', 'Home', 'Electronics',
                     'Fashion', 'Home', 'Electronics', 'Fashion', 'Home',
                     'Electronics', 'Fashion', 'Home', 'Electronics', 'Fashion'],
        'Price': [300, 150, 60, 40, 80, 90, 200, 50, 100, 350, 120, 80, 400, 60, 70, 250, 100, 110, 180, 90],
        'Items Sold': [10, 7, 20, 15, 12, 8, 6, 14, 9, 4, 10, 11, 5, 16, 13, 7, 9, 12, 8, 11]}

df = pd.DataFrame(data)

# Sub-challenge 1: Data Cleaning
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the raw sales data.
    
    :param df: The input DataFrame containing raw sales data.
    :return: The cleaned and preprocessed DataFrame.
    """


# Sub-challenge 2: Feature Engineering
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features from the existing data to enhance analysis.
    
    :param df: The input DataFrame containing cleaned sales data.
    :return: The DataFrame with new features added.
    """
    


# Sub-challenge 3: Data Aggregation
def aggregate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, str]:
    """
    Aggregate the data to answer specific questions or derive insights about the dataset.
    
    :param df: The input DataFrame containing cleaned and engineered sales data.
    :return: A tuple containing the aggregated data results.
    """
    
    

# Sub-challenge 4: Data Visualization
def visualize_data(df: pd.DataFrame, total_revenue_per_product: pd.DataFrame, avg_price_per_category: pd.DataFrame,
                   season_sales: pd.DataFrame) -> None:
    """
    Create visualizations to help better understand the dataset and communicate findings.
    
    :param df: The input DataFrame containing cleaned and engineered sales data.
    :param total_revenue_per_product: DataFrame containing total revenue per product.
    :param avg_price_per_category: DataFrame containing average price per category.
    :param season_sales: DataFrame containing sales by season.
    :return: None
    """
    
    


# Main function to execute the challenge
def main() -> None:
    cleaned_data = clean_data(df)
    engineered_data = engineer_features(cleaned_data)
    total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season = aggregate_data(engineered_data)
    visualize_data(engineered_data, total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season)


if __name__ == '__main__':
    main()