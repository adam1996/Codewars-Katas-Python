'''

Grasshopper - Messi goals function (8kyu)
https://www.codewars.com/kata/55f73be6e12baaa5900000d4

Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17
'''

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


# or

def goals(*a):
    return sum(a)

#*a can collect params as a tuple named a
#'**a can collect params as a dict named a
