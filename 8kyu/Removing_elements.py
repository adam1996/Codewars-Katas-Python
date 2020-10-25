"""

Removing Elements (8Kyu)
https://www.codewars.com/kata/5769b3802ae6f8e4890009d2

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:

my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
None of the arrays will be empty, so you don't have to worry about that!
"""


def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ]))
