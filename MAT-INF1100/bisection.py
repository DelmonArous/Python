from math import *

def f(x):
    return sin(x)

def bisection(f,a,b):
    
    if f(a)*f(b) > 0:
        return None, 0

    i = 0
    N = 9
    abserr = (b-a)/2.
    m = (a+b)/2.

    while i <= N: # and abserr > (eps*abs(m)):
        
        if f(m) == 0:
            a = b = m
        if f(a)*f(m) < 0:
            b = m
        else:
            a = m
        
        abserr = (b-a)/2.
        m = (a+b)/2.
        relerr = (b-a)/(abs(m)*2.**(i+1.))
        i += 1
        
        print 'iteration = %g: m = %.16f , absolute error = %g, relativ error = %g' % (i, m , abserr, relerr)
        
        
        
    return m, i

root, iteration = bisection(f,3,4)
