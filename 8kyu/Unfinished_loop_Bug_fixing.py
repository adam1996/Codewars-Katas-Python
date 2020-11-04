'''


Unfinished Loop - Bug Fixing #1 (8kyu)
https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

Unfinished Loop - Bug Fixing #1
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

'''


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


print(create_array(2))
