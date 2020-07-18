import collections
from collections import deque

d = deque(range(0, 10, 3))

print(type(d))
print(d.pop())
print(d.popleft())
print(d)

d.append(21)
d.appendleft(24)

d2 = deque(sorted(d))
print(d2)

d.extend(range(11, 20, 3))
print(d)

d.rotate(-2)
print(d)
