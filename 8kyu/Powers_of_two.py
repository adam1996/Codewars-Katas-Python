"""

Powers of 2 (8Kyu)
https://www.codewars.com/kata/57a083a57cb1f31db7000028

Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
"""
def powers_of_two(n):
    return[2**i for i in range(n+1)]

print(powers_of_two(2))
