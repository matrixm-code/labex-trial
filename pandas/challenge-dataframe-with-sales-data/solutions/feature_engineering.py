import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Sub-challenge 2: Feature Engineering
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features from the existing data to enhance analysis.
    
    :param df: The input DataFrame containing cleaned sales data.
    :return: The DataFrame with new features added.
    """
    
    # TODO: implement this function here.
    # Note: Do not change the existing code.
    df['Revenue'] = df['Price'] * df['Items Sold']
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    
    # Create 'Price Category'
    def price_category(price: float) -> str:
        if price <= 60:
            return 'Low'
        elif 60 < price <= 150:
            return 'Medium'
        else:
            return 'High'

    df['Price Category'] = df['Price'].apply(price_category)

    # Create 'Season'
    def season(month: int) -> str:
        if 3 <= month <= 5:
            return 'Spring'
        elif 6 <= month <= 8:
            return 'Summer'
        elif 9 <= month <= 11:
            return 'Fall'
        else:
            return 'Winter'

    df['Season'] = df['Month'].apply(season)

    return df

if __name__ == '__main__':
    df = pd.read_csv('dc.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    engineered_df = engineer_features(df)
    engineered_df=engineered_df.loc[:,~engineered_df.columns.str.contains("^Unnamed")]
    engineered_df.to_csv('ef.csv')
    print(engineered_df)
    