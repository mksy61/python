import numpy

A = numpy.random.permutation(numpy.arange(0, 20, 2))
B = A.reshape(2, 5)
C = numpy.random.permutation(numpy.arange(20, 40, 2))
D = C.reshape(2, 5)

print(B[1, 2])
print([A > 4])
print(A[(A < 12) & (A > 4)])
A = A*2
print(A)
A.sort()
print(A)
print("-"*40)
print(B)
print("-"*40)
print(D)
print("-"*40)
E = numpy.vstack(A)
print(E)
