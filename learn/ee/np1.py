import numpy
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta


l = list(range(1, 10000000))
timestampstart = datetime.now()
for i in l:
    pass
timestampsend = datetime.now()
print(timestampsend - timestampstart)

print()

n = numpy.array(range(1, 10000000), dtype="i")
timestampstart = datetime.now()
for i in n:
    pass
timestampsend = datetime.now()
print(timestampsend - timestampstart)
