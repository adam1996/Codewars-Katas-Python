'''

Simple multiplication (8kyu)
https://www.codewars.com/kata/583710ccaa6717322c000105/train/python

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
'''


def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9
