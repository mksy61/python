import numpy

a = numpy.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
b = numpy.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
                 [[5, 6, 7], [6, 7, 8], [7, 8, 9]]])
c = numpy.array([1, 3, 5, 7, 9])

print(a.dtype)
print(a.ndim)
print(a[0])

print("*"*40)

print(b.dtype)
print(b.ndim)
print(b[0])
print(b[0][0])
print(b[0][0][0])
print()

print(a.shape[0], a.shape[1])
print(b[0, 1, 2])
print()

print(a.shape)
print(b.shape)
print(c.shape)
print()

print(b.size)
print(b.nbytes)
print(b.all())
