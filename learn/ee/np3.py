import numpy

A = numpy.random.permutation(numpy.arange(12))
print(type(A))

B = A.reshape(3, 4)

print(B.shape)
print(B)

C = numpy.random.rand(5)
D = numpy.random.randn(5)

print(C)
print(D)
