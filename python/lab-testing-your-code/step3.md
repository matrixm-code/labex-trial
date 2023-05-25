# Testing with Databases

Finally, let's test some code that interacts with a database. For this example, we will use SQLite and the **sqlite3** module.

In **my_code.py**, create a function named **create_table** that creates a new table in an SQLite database.

```python
import sqlite3

def create_table():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()
```

In this code, we create a new SQLite database table named "my_table" with two columns: "id" and "name". We then define a test class named **TestCreateTable** with a **setUp** method that creates an SQLite database for testing.

Now let's write a test for the **create_table** function. First, we need to create a new database for testing. We will do this in a setup method that runs before each test.

```python
class TestCreateTable(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('my_database.db')

    def test_create_table(self):
        create_table()
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='my_table'")
        result = c.fetchone()
        self.assertIsNotNone(result)
```

In the **setUp** method, we create a new SQLite database.

In the **test_create_table** method, we call the **create_table** function and then check that the table was created using a SQL query.

Now we can run our tests again:

```
python -m unittest test_my_code.py
```

If the test passes, you should see output like the following:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

The **...** indicates that three tests passed.
