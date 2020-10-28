'''

noobCode 01: SUPERSIZE ME.... or rather, this integer! (8kyu)
https://www.codewars.com/kata/5709bdd2f088096786000008

Write a function that rearranges an integer into its largest possible value.

super_size(123456) # 654321
super_size(105)    # 510
super_size(12)     # 21
If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.

- sort only works for lists. Sorted() works for any iterable.
- https://docs.python.org/3/howto/sorting.html
- reverse = true

'''

def super_size(n):
    return int("".join(sorted(str(n), reverse = True)))

print(super_size(2456141))
