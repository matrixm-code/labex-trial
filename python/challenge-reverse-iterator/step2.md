# Python Reverse Iterator

The challenge in this step is to create an iterator in Python that implements the following methods:

- `init(self, data)`: Initialize the iterator with a list of integers data. The iterator will iterate over the elements of data in reverse order.
- `next(self)`: Return the next value from the iteration. Return None when the iteration has ended.
- `iter(self)`: Return the iterator object itself.

Example usage:

```python
>>> it = ReverseIterator([1, 2, 3, 4, 5])
>>> next(it)
5
>>> next(it)
4
>>> next(it)
3
>>> next(it)
2
>>> next(it)
1
>>> next(it)
None
```

## Init Method

```python
def __init__(self, data: list):
```

- In this method, initialize `self.data` with a list of integers `data`.
- `self.index` represents the position of the current iteration, and it should be initialized with the maximum subscript of the list `data`.

## Next Method

```python
def __next__(self) -> int:
    if condtion:
    else：
```

- In the `if` branch, return the next value from the iteration.`condition` is a boolean expression, which is used to judge whether the iteration has ended. Notice the change of `self.index`.
- In the `else` branch, return None when the iteration has ended.

## Iter Method

```python
def __iter__(self) -> 'ReverseIterator':
```

- Return the iterator object itself.

## TODO

- Completing `reverseiterator.py`

## Requirements

- Your implementation must be a class named `ReverseIterator`.
- You must implement the methods described above.
- Your implementation must be able to handle cases where the data list is `empty`.
- No modules can be imported.
