import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

df = pd.read_csv('dc.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Sub-challenge 2: Feature Engineering
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new features from the existing data to enhance analysis.
    
    :param df: The input DataFrame containing cleaned sales data.
    :return: The DataFrame with new features added.
    """
    
    # TODO: implement this function here.
    # Note: Do not change the existing code.

    df.to_csv('ef.csv')
    return

if __name__ == '__main__':
    engineered_df = engineer_features(df)
    print(engineered_df)

