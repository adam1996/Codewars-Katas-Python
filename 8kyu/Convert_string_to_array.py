'''

Convert a string to an array (8Kyu)
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

Write a function to split a string and convert it into an array of words. For example:

"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
'''


def string_to_array(s):
    return s.split() if s else [""]


print(string_to_array("Hello my name is"))
