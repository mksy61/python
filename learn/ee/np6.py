import numpy
from datetime import datetime


x = numpy.random.rand(100000000)

timestampstart = datetime.now()
print(numpy.sum(x))
timestampsend = datetime.now()
print(timestampsend - timestampstart)

timestampstart = datetime.now()
print(sum(x))
timestampsend = datetime.now()
print(timestampsend - timestampstart)
