import pandas

x = [1, 2, 3, 4, 5]
y = pandas.Series(x)

print(y)
print(y.index)
print(y.values)
print(y.dtype)
y.name = "Sayilar"

print(y)
