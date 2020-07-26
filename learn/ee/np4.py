import numpy

A = numpy.arange(0, 20, 2)
print(A)

B = A[2:5].copy()
C = numpy.round(numpy.random.rand(3, 5)*100)
B[0] = 222
print(id(A))
print(id(B))
print(C.shape)
print(A)
print(B)

print(A[::2])

print(numpy.argwhere(A == 4))

print(C[0, :])
print(C[:, 2])
