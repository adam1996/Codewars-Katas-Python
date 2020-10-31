'''

Sort and Star (8kyu)
https://www.codewars.com/kata/57cfdf34902f6ba3d300001e

You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
'''

def two_sort(array):

    return "***".join([i for i in (sorted(array)[0])])


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
