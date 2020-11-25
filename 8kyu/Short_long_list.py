"""
Short Long Short (8Kyu)
https://www.codewars.com/kata/50654ddff44f800200000007

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( length 0 ).

For example:

solution("1", "22") # returns "1221"
solution("22", "1") # returns "1221"

def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b
    
"""

def solution(a, b):
    input_lst = [a, b]
    input_lst.sort(key=len, reverse=False) 
    return input_lst[0] + input_lst[1] + input_lst[0]


print(solution("Adam", "Johnson"))