import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
import numpy as np
from data_cleaning import clean_data

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

    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertTrue(isinstance(cleaned_df, pd.DataFrame))

    def test_result(self):
        expected_data = {'Date': ['2021-03-01', '2021-03-02', '2021-03-03', '2021-05-04', '2021-05-05',
                            '2021-06-06', '2021-06-07', '2021-07-08', '2021-07-10', '2021-07-10',
                            '2021-07-11', '2021-07-11', '2021-09-14', '2021-10-15',
                            '2021-10-16', '2021-11-17'],
                    'Product': ['Product A', 'Product B', 'Product C', 'Product C', 'Product E',
                                'Product F', 'Product G', 'Product H', 'Product C', 'Product J',
                                'Product K', 'Product N', 'Product N', 'Product O',
                                'Product P', 'Product Q'],
                    'Category': ['Electronics', 'Electronics', 'Home', 'Fashion', 'Fashion',
                                'Home', 'Electronics', 'Fashion', 'Home', 'Electronics',
                                'Fashion', 'Electronics', 'Fashion', 'Home',
                                'Electronics', 'Fashion'],
                    'Price': [300, 150, 60, 40, 80, 90, 200, 50, 100, 350, 120, 400, 60, 70, 250, 100],
                    'Items Sold': [10, 7, 20, 15, 12, 8, 6, 14, 9, 4, 10, 5, 16, 13, 7, 9]}
        cleaned_df = clean_data(self.df)
        # pd.testing.assert_frame_equal(cleaned_df, cleaned_df, check_dtype=False)
        expected_data.assertEqual(cleaned_df)
        # pd.testing.assert_frame_equal(expected_data["Date"], cleaned_df["Date"])
        # pd.testing.assert_frame_equal(expected_data["Product"], cleaned_df["Product"])
        # self.assertTrue(pd.testing.assert_series_equal(expected_data["Category"], cleaned_df["Category"]))
        # self.assertTrue(pd.testing.assert_series_equal(expected_data["Price"], cleaned_df["Price"]))
        # self.assertTrue(pd.testing.assert_series_equal(expected_data["Items Sold"], cleaned_df["Items Sold"]))

if __name__ == '__main__':
    
    # cleaned_df = clean_data(self.df)
    # self.assertTrue(pd.testing.assert_series_equal(expected_data["Date"], cleaned_df["Date"]))
    # self.assertTrue(pd.testing.assert_series_equal(expected_data["Product"], cleaned_df["Product"]))
    # self.assertTrue(pd.testing.assert_series_equal(expected_data["Category"], cleaned_df["Category"]))
    # self.assertTrue(pd.testing.assert_series_equal(expected_data["Price"], cleaned_df["Price"]))
    # self.assertTrue(pd.testing.assert_series_equal(expected_data["Items Sold"], cleaned_df["Items Sold"]))
    unittest.main()