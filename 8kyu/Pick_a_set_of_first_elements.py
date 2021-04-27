"""

pick a set of first elements(8Kyu)
https://www.codewars.com/kata/572b77262bedd351e9000076

Write a function to get the first elements of asequence. Passing a parameter n (default=1) will return the first n elements of the sequence.

If n == 0 return an empty sequence []

Examples
arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
"""
def first(seq, n):
    return seq[:n] if n else []
