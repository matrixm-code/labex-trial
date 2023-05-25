# Add Numbers

## Setup

To get started, we need to create a new Python file for our tests. Let's call it **test_my_code.py**. We will also create a module that contains the code we want to test. Let's call this module **my_code.py**.

## Simple Test

Let's start with a simple function that returns the sum of two numbers. In **my_code.py**, create a function named **add_numbers** that takes two arguments and returns their sum.

```python
def add_numbers(a, b):
    return a + b
```

Now let's write a test for this function in **test_my_code.py**. First, we need to import the **unittest** module and the **add_numbers**function.

```python
import unittest
from my_code import add_numbers
```

Next, we will create a class named **TestAddNumbers** that inherits from **unittest.TestCase**.

```python
class TestAddNumbers(unittest.TestCase):
    pass
```

Inside this class, we will create a method named **test_add_numbers** that will test the **add_numbers** function. We will use the **assertEqual** method to check that the function returns the correct sum.

```python
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
```

Now we can run our tests using the following command:

```
python -m unittest test_my_code.py
```

If the test passes, you should see output like the following:

```
...
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

The **.** indicates that one test passed.
