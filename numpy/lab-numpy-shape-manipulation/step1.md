# Reshaping Arrays

The `reshape` function allows you to change the shape of a NumPy array. The syntax of the `reshape` function is as follows:

```python
np.reshape(a, new_shape)
```

- where `a` is the input array and `new_shape` is the desired new shape of the array.

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Import NumPy

NumPy is already installed，you can import it in your Python code:

```python
import numpy as np
```

## Create an Array

Create an array `a` of shape (2, 3) as an example:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
```

Output:

```python
(2, 3)
```

## Using Reshape

You can reshape this array to a shape of (3, 2) using the `reshape` function:

```python
b = np.reshape(a, (3, 2))
print(b.shape)
print(b)
```

Output:

```python
(3, 2)
[[1 2]
 [3 4]
 [5 6]]
```
