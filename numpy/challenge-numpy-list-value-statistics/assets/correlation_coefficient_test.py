import sys

sys.path.append("/home/labex/project")

import unittest
from correlation_coefficient import correlation_coefficient
from unittest.mock import patch


class TestCorrelationCoefficient(unittest.TestCase):
    def test_correlation_coefficient_results(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        expected_output = 0.9999999999999999
        self.assertEqual(correlation_coefficient(x, y), expected_output)

    @patch("numpy.corrcoef")
    def test_correlation_coefficient_use(self, mock_corrcoef):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        correlation_coefficient(x, y)
        mock_corrcoef.assert_called_once_with(x, y)


if __name__ == "__main__":
    unittest.main()
