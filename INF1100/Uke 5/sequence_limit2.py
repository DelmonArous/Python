from numpy import *
import sys

try:
    N = int(sys.argv[1])
except IndexError: 
    print 'You failed to provide cml argument!'
    N = int(raw_input('N=? '))

index_set = range(N+1)
D = zeros(N+1)

for n in index_set:
    D[n] = sin(2**(-n))/(2**(-n))
    print 'D[%d] = %g' % (n,D[n])

print 'Exact limit: ', 1
    
