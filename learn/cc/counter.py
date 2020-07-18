import collections
from collections import Counter

c = Counter("deneme")

print(c)

c = Counter([1, 3, 5, 7, 1, 1, 3])
print(c)

c = Counter({"a": 1, "b": 2, "c": 3, "d": 4})
print(c)

d = Counter("e")
c.subtract(d)
print(c)
