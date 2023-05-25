import sys

sys.path.append("/home/labex/project")

import unittest
from standard_deviation import standard_deviation
from unittest.mock import patch


class TestStandardDeviation(unittest.TestCase):
    def test_standard_deviation_results(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = 2.8722813232690143
        self.assertEqual(standard_deviation(numbers), expected_output)

    @patch("numpy.std")
    def test_standard_deviation_use(self, mock_std):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        standard_deviation(numbers)
        mock_std.assert_called_once_with(numbers)


if __name__ == "__main__":
    unittest.main()
