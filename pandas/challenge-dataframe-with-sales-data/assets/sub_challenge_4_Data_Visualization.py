import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple
from sub_challenge_1_Data_Cleaning import data

df = pd.DataFrame(data)

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
    
    # TODO: implement this function here.
    # Note: Do not change the existing code.