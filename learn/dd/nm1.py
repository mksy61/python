import numpy as np

x = np.arange(4)**2
print(type(x))


y = np.random.rand(16)
y = y.reshape(4, 4)

print(y[0])
print(y[0][3])
