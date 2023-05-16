import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

# Sub-challenge 1: Data Cleaning
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the raw sales data.
    
    :param df: The input DataFrame containing raw sales data.
    :return: The cleaned and preprocessed DataFrame.
    """

    # TODO: implement this function here.
    # Note: Do not change the existing code.

    return

if __name__ == '__main__':   
    # Load sample data
    data = {'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-05-04', '2021-05-05',
                    '2021-06-06', '2021-06-07', '2021-07-08', '2021-07-10', '2021-07-10',
                    '2021-07-11', '2021-07-11', '2021-07-11', '2021-09-14', '2021-10-15',
                    '2021-10-16', '2021-11-17', '2021-12-18', '2021-12-19', np.nan],
            'Product': ['Product A', 'Product B', 'Product C', 'Product C', 'Product E',
                        'Product F', 'Product G', 'Product H', 'Product C', 'Product J',
                        'Product K', 'Product N', 'Product N', 'Product N', 'Product O',
                        'Product P', 'Product Q', np.nan, np.nan, 'Product T'],
            'Category': ['Electronics', 'Electronics', 'Home', 'Fashion', 'Fashion',
                        'Home', 'Electronics', 'Fashion', 'Home', 'Electronics',
                        'Fashion', 'Electronics', 'Electronics', 'Fashion', 'Home',
                        'Electronics', 'Fashion', 'Home', 'Electronics', 'Fashion'],
            'Price': [300, 150, 60, 40, 80, 90, 200, 50, 100, 350, 120, 400, 400, 60, 70, 250, 100, 110, 180, 90],
            'Items Sold': [10, 7, 20, 15, 12, 8, 6, 14, 9, 4, 10, 5, 5, 16, 13, 7, 9, np.nan, 8, 11]}

    df = pd.DataFrame(data)
    clean_df = clean_data(df)
    clean_df.to_csv('dc.csv')
    print(clean_df)