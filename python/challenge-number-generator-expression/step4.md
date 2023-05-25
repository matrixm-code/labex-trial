# Fibonacci Numbers Generator

The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence goes as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on. In mathematical terms, the `n`th Fibonacci number is defined as:

```scss
F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1
```

Write a function `fibonacci` that takes an integer as input and returns a generator that yields the first Fibonacci numbers.

## TODO

- Completing `fibonacci.py`

## Requirements

- The function should take an integer n as input, where n is the number of Fibonacci numbers to generate.
- The function should return a generator that yields the first n Fibonacci numbers.
- The generator should not store the entire list of Fibonacci numbers in memory. Instead, it should yield each Fibonacci number one at a time.
