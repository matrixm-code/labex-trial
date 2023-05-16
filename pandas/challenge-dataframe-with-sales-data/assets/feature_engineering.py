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

    return

if __name__ == '__main__':
    df = pd.read_csv('dc.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    engineered_df = engineer_features(df)
    engineered_df=engineered_df.loc[:,~engineered_df.columns.str.contains("^Unnamed")]
    engineered_df.to_csv('ef.csv')
    print(engineered_df)

