"""
Small enough? - Beginner! (7Kyu)
https://www.codewars.com/kata/57cc981a58da9e302a000214

You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value.
If they are, return true. Else, return false.

You can assume all values in the array are numbers.

def small_enough(array, limit):
    return max(array)<=limit

"""
def small_enough(array, limit):
    return not any([val > limit for val in array])

print(small_enough([100] ,100))
#(false, true, true, true )

