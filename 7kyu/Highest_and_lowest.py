'''

Highest and Lowest (7Kyu)
https://www.codewars.com/kata/554b4ac871d6813a03000035


In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))
'''


def high_and_low(numbers):
    nums = numbers.split()  # split the string of space seperated nums into a new list
    x = list(map(int, nums))  # convert string items in new nums list to ints in order to return max and min values.
    return str(max(x)) + " " + str(min(x))


print(high_and_low("1 2 3 4 5"))