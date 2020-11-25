"""

Is it even? (8Kyu)
https://www.codewars.com/kata/555a67db74814aa4ee0001b5 

In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats are considered UNeven for this kata.
"""

def is_even(n): 
    print(type(n))
    return isinstance(n, int) and  n % 2 == 0 

print(is_even(2))