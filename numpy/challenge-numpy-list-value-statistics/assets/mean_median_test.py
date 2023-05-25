import sys

sys.path.append("/home/labex/project")

import unittest
from mean_median import mean_median
from unittest.mock import patch


class TestMeanMedian(unittest.TestCase):
    def test_mean_median_result(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = (5.5, 5.5)
        self.assertEqual(mean_median(numbers), expected_output)

    @patch("numpy.mean")
    @patch("numpy.median")
    def test_mean_median_use(self, mock_mean, mock_median):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        mean_median(numbers)
        mock_mean.assert_called_once_with(numbers)
        mock_median.assert_called_once_with(numbers)


if __name__ == "__main__":
    unittest.main()
