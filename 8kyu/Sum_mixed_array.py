'''

Sum Mixed Array(8kyu)
https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

'''

def sum_mix(arr):
    #int_arr = [int(i) for i in arr]
    #return sum(map(int, arr)) #Carries out int() on each item of the iterable 'arr'. 

    return sum(int(i) for i in arr)

print(sum_mix([9, 3, '7', '3']))
