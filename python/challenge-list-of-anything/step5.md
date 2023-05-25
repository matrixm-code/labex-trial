# Product of Numbers

Given two lists of numbers, write a list comprehension that creates a new list containing the product of each pair of numbers from the corresponding positions in the original lists.

The syntax of a list comprehension is:

```python
new_list = [out_expression for item1,item2 in func(list1,list2)]
```

- `func(list1,list2)` is a fuction that packs the corresponding elements of the original list into a tuple and returns a list of these tuples.
- `item1` and `item2` are the elements of the tuple.
- `out_expression` is the product of `item1` and `item2`.

## TODO

- Completing `product_of_numbers.py`

## Requirements

- Use only the list comprehensions to solve the problem.
- No modules can be imported.
