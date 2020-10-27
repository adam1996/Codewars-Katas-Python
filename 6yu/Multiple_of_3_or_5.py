"""
Multiples of 3 or 5 (6Kyu)
https://www.codewars.com/kata/514b92a657cdc65150000006

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(number):
    temp = []

    for i in range(number):
        if i % 3 == 0:
            temp.append(i)
        elif i % 5 == 0:
            temp.append(i)

    return sum(temp)


print(solution(10))
