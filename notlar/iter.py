l = list(range(0, 10))


def sq(x):
    return x**2


a = [sq(x) for x in l]
b = tuple(sq(x) for x in l if x % 2 == 0)

print(a, " ", type(a))
print(b, " ", type(b))
