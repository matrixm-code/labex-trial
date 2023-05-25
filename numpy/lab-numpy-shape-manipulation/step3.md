# Transposing Arrays

The `transpose` function allows you to transpose the axes of a NumPy array. The syntax of the `transpose` function is as follows:

```python
a.transpose([axis1, axis2, ...])
```

- where `axis1`, `axis2`, etc. are the axes to be transposed.

## Create an Array

create an array `a` of shape (2, 3) as an example:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
```

Output:

```python
[[1 2 3]
 [4 5 6]]
(2, 3)
```

## Using Transpose

You can transpose this array using the `transpose` function:

```python
b = a.transpose()
print(b)
print(b.shape)
```

Output:

```python
[[1 4]
 [2 5]
 [3 6]]
(3, 2)
```

You can also transpose specific axes of the array. For example, you can transpose the axes of the array `a` to have a shape of (3, 2) using the following code:

```python
c = a.transpose(1, 0)
print(c)
print(c.shape)
```

Output:

```python
[[1 4]
 [2 5]
 [3 6]]
(3, 2)
```
