import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
import numpy as np
from data_cleaning import clean_data
from feature_engineering import engineer_features
from data_aggregation import aggregate_data
from data_visualization import visualize_data

class TestAdvancedPandasChallenge(unittest.TestCase):

    def setUp(self):
        self.data = {'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-05-04', '2021-05-05',
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

        self.df = pd.DataFrame(self.data)

    # No assertion for visualization function, as it generates plots
    def test_visualize_data(self):
        cleaned_df = clean_data(self.df)
        engineered_df = engineer_features(cleaned_df)
        total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season = aggregate_data(engineered_df)
        visualize_data(engineered_df, total_revenue_per_product, avg_price_per_category, top_10_products, engineered_df.groupby('Season')['Revenue'].sum().reset_index())

if __name__ == '__main__':
    unittest.main()