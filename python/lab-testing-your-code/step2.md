# Testing Exceptions

Next, let's test a function that raises an exception. In **my_code.py**, create a function named **divide** that takes two arguments and returns their quotient. If the second argument is zero, the function should raise a **ZeroDivisionError**.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b
```

Now let's write a test for this function in **test_my_code.py**. We will use the **assertRaises** method to check that the function raises a **ZeroDivisionError** when the second argument is zero.

```python
class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
```

Now we can run our tests again:

```
python -m unittest test_my_code.py
```

If the test passes, you should see output like the following:

```
...
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

The **..** indicates that two tests passed.
