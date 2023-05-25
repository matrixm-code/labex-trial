# Indexing with Boolean Arrays

Boolean indexing is a powerful feature that allows us to filter an array based on a condition. You can create a boolean array by applying a logical operator to an existing array.

## Create a 1-dimensional Array

```python
c = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

## Create a Boolean Array Based on the Condition (c > 5)

```python
mask = c > 5
print(mask)
```

Output:

```python
[False False False False False False  True  True  True  True]
```

## Filter the Original Array Using the Boolean Array

```python
print(c[mask])
```

Output:

```python
[6 7 8 9]
```
