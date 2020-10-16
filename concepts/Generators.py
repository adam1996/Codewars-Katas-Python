'''
Concept: Generators.
Link: Expert Python Tutorial #5- Generators. (Youtube: )

1) Computers have a finite amount of memory/RAM.
2) When we run our programs data is manipulated and stored in memory.
3) We are therefore limited by the amount of RAM in our computer.
4) It is possible to exceed this limit by calculating and printing the square of each num in the range of a million.
5) We get a memory error!
6) Generators can avoid this for us.

    x = [i**2 for i in range(100000000000)]

    for i in x:
        print(i)

- Processing 1 item at time. Is it necessary to make a list?

    for i in range(100000)
        print(i**2)

- Generators allow us to process one value at a time without having to create a list for them.

'''

class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0 #use this var to keep track of the last number we squared.

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2 #our return val is going to be equal to our previous value squared.
        self.last += 1
        return rv


g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break

#We only store the last val we generated and then we use that to generate the next, and so on so fourth.
