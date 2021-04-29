"""
Find the stray number (7Kyu)
https://www.codewars.com/kata/57f609022f4d534f05000024

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""

def stray(arr):
    for i in arr:
        if arr.count(i): return i
