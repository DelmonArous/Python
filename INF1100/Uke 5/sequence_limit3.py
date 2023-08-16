from scitools.std import *

def D(f, x, N):
    
    index_set = range(N)
    D = zeros(N)
   
    for n in index_set:
        h = 2**(-n)
        D[n] = (f(x + h)-f(x))/float(h)
        print 'D[%d] = %g' % (n, D[n])
    
    return D

Dn = D(sin, pi, 80)

plot(range(len(Dn)), Dn,
     xlabel='n',ylabel='D[n]')
