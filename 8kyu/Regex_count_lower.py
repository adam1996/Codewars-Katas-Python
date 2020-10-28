'''

Regex count lowercase letters (8kyu)
https://www.codewars.com/kata/56a946cd7bd95ccab2000055

Your task is simply to count the total number of lowercase letters in a string.

Examples
lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123"); ===> 3

lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3

lowercaseCount(""); ===> 0;

lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0

lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26

def lowercase_count(strng):
    return sum(a.islower() for a in strng)

'''
def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.islower(): count += 1
    return count
