# Concatenating and Splitting Arrays

NumPy provides two functions for concatenating arrays:

1. np.concatenate: for concatenating arrays along a given axis
2. np.stack: for concatenating arrays along a new axis

You can split arrays using the `np.split` function.

## Concatenating Arrays

Create two arrays `a` and `b` as an example:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

### Using Concatenate

You can concatenate these arrays along the first axis(0) using the `np.concatenate `function:

```python
c = np.concatenate((a, b))
print(c)
```

Output:

```python
[1 2 3 4 5 6]
```

### Using Stack

You can also concatenate these arrays along a new axis using the `np.stack` function:

```python
d = np.stack((a, b))
print(d)
print(d.shape)
```

Output:

```python
[[1 2 3]
 [4 5 6]]
(2, 3)
```

## Splitting Arrays

Create an array `a` of shape (6,) as an example:

```python
a = np.array([1, 2, 3, 4, 5, 6])
```

### Using Split

You can split this array into two arrays of length 3 using the `np.split` function:

```python
b, c = np.split(a, 2)
print(b)
print(c)
```

Output:

```python
[1 2 3]
[4 5 6]
```
