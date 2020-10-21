'''

Count Odd Numbers below n (8Kyu)
https://www.codewars.com/kata/59342039eb450e39970000a6

Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
Expect large Inputs!
'''


def odd_count(n):
    odd_count = 0
    for i in range(n):
        if i % 2 == 1: odd_count += 1

    return odd_count


print(odd_count(15))

def oddCount(n):
    return n // 2
