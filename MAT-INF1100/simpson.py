from math import *

def f(x):
    return exp(x)

a = 0.; b = 1.
n = 10; h = (b-a)/n
I = 0; x = a

for k in range(1,n+1):
    I += (h/3.)*(f(x-2*h)+4*f(x-h)+f(x))
    x += k*h

j = 1
abserr = abs(I)
eps = 1E-17

while j < 15  and abserr > eps*abs(I):
    j += 1
    Ip = I
    n = 2*n; h = (b-a)/n
    I = 0; x = a
    
    for k in range(1,n+1):
        I += (h/3.)*(f(x-2*h)+4*f(x-h)+f(x))
        x += k*h

    abserr = abs(I-Ip)
    print 'Iteration: %g, step length: %.16f, approx.: %.16f, absolute error: %g' % (j,h, I, abserr)
