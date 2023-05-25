# Random Number Generation

NumPy provides several functions to generate random numbers. Here are a few examples:

## Generating Random Numbers

The `np.random.rand()` function can be used to generate random numbers between 0 and 1.

```python
# generate a 2x2 matrix of random numbers
a = np.random.rand(2, 2)

print(a) # Output: [[0.43584547 0.37752558], [0.08936734 0.65526767]]
```

## Generating Random Integers

The `np.random.randint()` function can be used to generate random integers between two specified numbers.

```python
# generate an array of random integers between 1 and 10
a = np.random.randint(1, 10, size=(3, 3))

print(a) # Output: [[8 7 3], [3 3 7], [8 8 7]]
```

## Generating Normal Distribution

The `np.random.normal()` function can be used to generate numbers from a normal distribution.

```python
# generate an array of numbers from a normal distribution
a = np.random.normal(0, 1, size=(2, 2))

print(a) # Output: [[ 1.28418331 -0.90564647], [-0.76477896  1.69903421]]
```

## Exercise

Now please follow the above functions to complete the output of random number, random integer and normal distribution.Please complete this exercise.
