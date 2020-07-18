x = list(range(0, 16))


def isOdd(n):
    return n % 2 != 0


y = list(filter(isOdd, x))

print(y)
