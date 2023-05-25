# Read and Count

There are some JSON files in the `home/labex/json_files` folder, all the keys are string objects.

Try to read them all and count how many elements are in them by the Python script `count.py`

For example, there are three elements in the below JSON data structure:

```json
{
  "1": [1, 2],
  "2": "abc",
  "3": { "a": "b" }
}
```

1. The first element is a key-value pair where the key is `"1"` and the value is an array `[1, 2]`.
2. The second element is a key-value pair where the key is `"2"` and the value is a string `"abc"`.
3. The third element is a key-value pair where the key is `"3"` and the value is an object with a single key-value pair where the key is `"a"` and the value is `"b"`.

## Requirements

- The path of `count.py` is `/home/labex/project`.
- The count result should be `print` in the console.
