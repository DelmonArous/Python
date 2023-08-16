import sys
from math import *

i1 = eval(sys.argv[1])
i2 = eval(sys.argv[2])

r = i1 + i2

print '%s + %s becomes %s with value %s' % \
      (type(i1), type(i2), type(r), r)
