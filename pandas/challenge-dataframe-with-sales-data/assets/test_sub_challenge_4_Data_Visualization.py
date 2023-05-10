import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
import numpy as np
from sub_challenge_1_Data_Cleaning import clean_data
from sub_challenge_2_Feature_Engineering import engineer_features
from sub_challenge_3_Data_Aggregation import aggregate_data
from sub_challenge_4_Data_Visualization import visualize_data

class TestAdvancedPandasChallenge(unittest.TestCase):

    # No assertion for visualization function, as it generates plots
    def test_visualize_data(self):
        cleaned_df = clean_data(self.df)
        engineered_df = engineer_features(cleaned_df)
        total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season = engineered_df.groupby('Season')['Revenue'].sum().reset_index()
        visualize_data(engineered_df, total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season)

if __name__ == '__main__':
    unittest.main()