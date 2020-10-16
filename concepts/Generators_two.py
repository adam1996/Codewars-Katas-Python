def gen(n):
    for i in range(n):
        yield i ** 2  # returns this value and pauses this executation, it does not stop it. It keeps track of all of the internal information in memory, i and n. Yield is a pause of execution and return is a stop.


g = gen(1000000)

for i in g:
    print(i)
