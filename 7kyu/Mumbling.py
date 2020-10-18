"""
Mumbling (7kyu)
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

Breakdown:

1) sep = '-'
2) Print each letter of string times by it's position in the string + 1, print(a*currentindex + 1)....
"""

#def accum(s):
#    for count, lett in enumerate(s):
#        print(lett.upper() + lett*count, end="-")
#    x = [lett.upper() + (lett * count) for count, lett in enumerate(s)]
#    return ''.join(x)

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum('Z-Pp-Ggg-Llll-Nnnnn-RRRRRR-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-UUUUUUUUUUU'))
