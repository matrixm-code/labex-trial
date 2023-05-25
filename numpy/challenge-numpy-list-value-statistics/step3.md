# Correlation Coefficient

In this sub-challenge, you will write a Python function that takes two lists of numbers as input and returns the correlation coefficient between the two lists using NumPy.

Examples:

```python
from correlation_coefficient import correlation_coefficient

# Example 1
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
corr_coef = correlation_coefficient(x, y)
print("Correlation Coefficient:", corr_coef)

# Example 2
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
corr_coef = correlation_coefficient(x, y)
print("Correlation Coefficient:", corr_coef)
```

Output:

```python
Correlation Coefficient: 1.0
Correlation Coefficient: -1.0
```

## Calculate Correlation Coefficient

The `numpy.corrcoef(x, y)` function is used to calculate the correlation coefficient between two lists of numbers.

- This function returns a correlation coefficient matrix of two lists `x` and `y`, where all the diagonal values are one.
- The correlation coefficient between two lists `x` and `y` is at position [0,1] or [1,0] of the matrix.

## TODO

- Completing `correlation_coefficient.py`

## Requirements

- Create a function called `correlation_coefficient` that takes two lists of numbers as input.
- Use NumPy to calculate the correlation coefficient between the two lists.
- Return the correlation coefficient.
