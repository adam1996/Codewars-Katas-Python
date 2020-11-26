"""
Can we divide it? (8 kyu)

https://www.codewars.com/kata/5a2b703dc5e2845c0900005a

Your task is to create function isDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.


"""


def is_divide_by(number, a, b):
    return True if number % a == 0 and number % b == 0 else False


# Better Solution:
# return number % a and number % b == 0


print(is_divide_by(-12, 2, -4))
