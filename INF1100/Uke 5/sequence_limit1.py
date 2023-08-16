from numpy import *
import sys

try:
    N = int(sys.argv[1])
except IndexError:
    print 'You failed to provide cml argument'
    N = int(raw_input('N=? '))

index_set = range(1,N+1)
a = zeros(N+1)

for n in index_set:
    a[n] = (7+(1./n))/(3-(1./n**2))
    print 'a[%d] = %g' % (n,a[n])

print 'Exact limit: ', 7./3


