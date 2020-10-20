"""

Double Char (8Kyu)
https://www.codewars.com/kata/56b1f01c247c01db92000076

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "
Good Luck!

"""


def double_char(s):
    return ''.join(i * 2 for i in s)


print(double_char("String"))
