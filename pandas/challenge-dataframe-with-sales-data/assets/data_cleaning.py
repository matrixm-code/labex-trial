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

    # TODO: implement this function here.
    # Note: Do not change the existing code.