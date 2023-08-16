from numpy import *

for i in [1, 2, 3, 6]:
    N = 10**i
    r = random.random(N)
    r1 = r[r > 0.5]
    r2 = r1[r1 <= 0.6].size
    print 'N = %d: probability: %g %%' % (N, (float(r2)/N)*100)
