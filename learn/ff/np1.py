import numpy

a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2]])
print(a[[True, False, True, False, True, False, True, False, True]])
a = a.reshape(3, 3)

print(a[:, 0:1])
print(a.sum())

print(a)
