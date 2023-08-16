from numpy import *
import sys

N = int(sys.argv[1])
r = random.random(N)
heads = r[r <= 0.5].size

print 'Flipping a coin %d times gave %d heads' % (N, heads)
