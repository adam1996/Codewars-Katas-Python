"""

Descending Order(7Kyu)
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
"""


def descending_order(num):
    #return int("".join(sorted(str(num), reverse=True)))
    return int(''.join(map(str, sorted([int(val) for val in [i for i in str(num)]], reverse=True))))


print(descending_order(42145))
