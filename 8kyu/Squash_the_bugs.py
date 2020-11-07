'''

Squash the bugs (8kyu)
https://www.codewars.com/kata/56f173a35b91399a05000cb7

Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value.
 Output should be the length of the longest word, as a number.

There will only be one 'longest' word.
'''
def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0

    while i < len(spl):
        if len(spl[i]) > longest: longest = len(spl[i])
        i += 1
    return longest


print(find_longest("The quick white fox jumped around the massive dog"))
