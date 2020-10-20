"""

The Feast of Many Beasts (8Kyu)
https://www.codewars.com/kata/5aa736a455f906981800360d

All of the animals are having a feast! Each animal is bringing one dish.
There is just one rule: the dish must start and end with the same letters as the animal's name.
For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

Assume that beast and dish are always lowercase strings, and that each has at least two letters.
beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.

True if beast[0] == dish[0] and beast[-1] == dish[-1]
- First letter of beast must be the same as the first letter of the dish
- Last letter of beast must be the same as the last letter of the dish
"""
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

print(feast("cat", "chicken"))
