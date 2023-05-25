# Fancy Indexing

Fancy indexing is a way of indexing an array using an array of indices. You can use this technique to extract specific elements or subsets of an array.

```python
# create a 1-dimensional array
d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# create an array of indices
indices = np.array([1, 3, 5])

# use fancy indexing to extract the elements at the specified indices
print(d[indices])
```

Output:

```python
[1 3 5]
```

- You can also use fancy indexing to assign values to specific elements in an array.

```python
# create a 1-dimensional array
e = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# create an array of indices
indices = np.array([1, 3, 5])

# assign the value 10 to the elements at the specified indices
e[indices] = 10
print(e)
```

Output:

```python
[ 0 10  2 10  4 10  6  7  8  9]
```
