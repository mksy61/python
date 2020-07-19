import sys


def gen(n):
    for i in range(n):
        yield i**2


h = [i**2 for i in range(10000000)]
g = gen(10000000)

print(sys.getsizeof(g))
print(sys.getsizeof(h))
