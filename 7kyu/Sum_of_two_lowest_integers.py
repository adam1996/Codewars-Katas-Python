"""
Sum of two lowest positive integers (7Kyu)
https://www.codewars.com/kata/558fc85d8fd1938afb000014

Challenge:

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
 No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

https://realpython.com/python-sort/#ordering-values-with-sort

Look into the difference between list.sort() and sorted(iter)
"""


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers [1]



print(sum_two_smallest_numbers([12, 10, 343445353, 3453445, 3453545353453]))
