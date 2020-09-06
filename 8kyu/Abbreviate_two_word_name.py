'''

Abreviate a Two Word Name
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
+ The output should be two capital letters with a dot separating them.
+ Sam Harris => S.H
+ Patrick Feeney => P.F

'''


def abbrev_name(name):
    # return '.'.join([x for x in name if x.isupper()])
    # join() method takes an iterable, in this case the array of upper case initlas from name, and joins them to a sep ('.')
    return '.'.join(w[0] for w in name.split()).upper()


print(abbrev_name("Sam Harris"))  # Should return "S.H"
