# Python Iterator

The challenge in this step is to create an iterator in Python that implements the following methods:

- `init(self,start,end)`: Initialize the iterator with two integer arguments start and end (0 <= start <= end). The iterator will iterate from start to end, and the end is inclusive.

- `next(self)`: Return the next value from the iteration. Return None when the iteration has ended.

- `iter(self)`: Return the iterator object itself.

Example usage:

```python
>>> it = >>> it = MyIterator(2, 5)
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)
5
>>> next(it)
None
```

## Init Method

```python
def __init__(self, start: int, end: int):
```

- In this method, initialize `self.start` and `self.end` with two integer arguments `start` and `end`.
- `self.current` represents the element currently being iterated over, and it should be initialized with the first element of the iterator.

## Next Method

```python
def __next__(self) -> int:
    if condtion:
    else：
```

- In the `if` branch, return the next value from the iteration.`condition` is a boolean expression, which is used to judge whether the iteration has ended. Notice the change of `self.current`.
- In the `else` branch, return None when the iteration has ended.

## Iter Method

```python
def __iter__(self) -> 'MyIterator':
```

- Return the iterator object itself.

## TODO

- Completing `myiterator.py`

## Requirements

- Your implementation must be a class named `MyIterator`.
- You must implement the methods described above.
- Your implementation must be able to handle cases where start and end are equal.
- Your implementation should be able to handle cases where start and end are both 0.
- No modules can be imported.
