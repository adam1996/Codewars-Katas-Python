'''

Find the first non-consecutive number (8kyu)
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole array is consecutive then return null2.

The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

If you like this Kata, maybe try this one next: https://www.codewars.com/kata/represent-array-of-numbers-as-ranges

Check out better solution using enumerate function:
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]
'''


def first_non_consecutive(arr):
    prev = -999999

    for val in arr:
        if prev == -999999 or val == (prev + 1):
            prev = val
        else:
            return val


print((first_non_consecutive([1, 2, 3, 4, 6, 7, 8])))
