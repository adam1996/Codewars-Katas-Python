"""
Get the mean of an Array. (8 kyu)
https://www.codewars.com/kata/563e320cee5dddcf77000158

Return the average of the given array rounded down to its nearest integer.

Conditions:

Array is never empty.

"""


def get_average(marks):
    return sum(marks) // len(marks)


marks = [2, 2, 2, 2]
print(get_average(marks))
