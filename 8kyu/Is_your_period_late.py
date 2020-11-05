"""
Is your period late? (8Kyu)
https://www.codewars.com/kata/578a8a01e9fd1549e50001f1

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days

Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.
"""
def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length


print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35))
