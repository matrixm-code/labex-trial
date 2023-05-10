import unittest
import pandas as pd
import numpy as np
#from dataframe_with_sales_data_script import clean_data, engineer_features, aggregate_data, visualize_data
from sub_challenge_1_Data_Cleaning import clean_data
from sub_challenge_2_Feature_Engineering import engineer_features
from sub_challenge_3_Data_Aggregation import aggregate_data
from sub_challenge_4_Data_Visualization import visualize_data


class TestAdvancedPandasChallenge(unittest.TestCase):

    def setUp(self):
        self.data = {'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-03-04', '2021-03-05',
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

        self.df = pd.DataFrame(self.data)

    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertTrue(isinstance(cleaned_df, pd.DataFrame))

    def test_engineer_features(self):
        cleaned_df = clean_data(self.df)
        engineered_df = engineer_features(cleaned_df)
        self.assertTrue(isinstance(engineered_df, pd.DataFrame))

    def test_aggregate_data(self):
        cleaned_df = clean_data(self.df)
        engineered_df = engineer_features(cleaned_df)
        results = aggregate_data(engineered_df)
        self.assertEqual(len(results), 4)
        self.assertTrue(isinstance(results[0], pd.DataFrame))
        self.assertTrue(isinstance(results[1], pd.DataFrame))
        self.assertTrue(isinstance(results[2], pd.DataFrame))
        self.assertTrue(isinstance(results[3], str))

    # No assertion for visualization function, as it generates plots
    def test_visualize_data(self):
        cleaned_df = clean_data(self.df)
        engineered_df = engineer_features(cleaned_df)
        total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season = engineered_df.groupby('Season')['Revenue'].sum().reset_index()
        visualize_data(engineered_df, total_revenue_per_product, avg_price_per_category, top_10_products, highest_sales_season)

if __name__ == '__main__':
    unittest.main()