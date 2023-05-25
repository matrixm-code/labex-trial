# Standard Deviation

In this sub-challenge, you will write a Python function that takes a list of numbers as input and returns the standard deviation of the numbers using NumPy.
Examples:

```python
from standard_deviation import standard_deviation

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
std_dev = standard_deviation(numbers)
print("Standard Deviation:", std_dev)

# Example 2
numbers = [3, 4, 6, 7, 8, 8, 9, 9, 9, 10]
std_dev = standard_deviation(numbers)
print("Standard Deviation:", std_dev)
```

Output:

```python
Standard Deviation: 2.8722813232690143
Standard Deviation: 2.1147629234082532
```

## Calculate Standard Deviation

The `numpy.std(list)` function is used to calculate the standard deviation of a list of numbers.

## TODO

- Completing `standard_deviation.py`

## Requirements

- Create a function called `standard_deviation` that takes a list of numbers as input.
- Use NumPy to calculate the standard deviation of the list.
- Return the standard deviation.
