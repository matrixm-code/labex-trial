# Mean and Median

In this sub-challenge, you will write a Python function that takes a list of numbers as input and returns the mean and median of the numbers using NumPy.

Examples:

```python
from mean_median import mean_median

# Example 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean, median = mean_median(numbers)
print("Mean:", mean)
print("Median:", median)

# Example 2
numbers = [3, 4, 6, 7, 8, 8, 9, 9, 9, 10]
mean, median = mean_median(numbers)
print("Mean:", mean)
print("Median:", median)
```

Output:

```python
Mean: 5.5
Median: 5.5
Mean: 7.3
Median: 8.0
```

## Calculate Mean

The `numpy.mean(list)` function is used to calculate the mean of a list of numbers.

## Calculate Median

The `numpy.median(list)` function is used to calculate the median of a list of numbers.

## TODO

- Completing `mean_median.py`

## Requirements

- Create a function called `mean_median` that takes a list of numbers as input.
- Use NumPy to calculate the mean of the list.
- Use NumPy to calculate the median of the list.
- Return a tuple containing the mean and median.
