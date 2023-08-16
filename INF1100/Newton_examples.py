from scitools.std import *
import sys

def Newton(f, x, dfdx, eps=1.0E-7, N=100, store=False):
    
    f_value = f(x)
    dfdx_value = float(dfdx(x))
    n = 0
    if store: info = [(x,f_value)]
    
    while abs(f_value) > eps and  n <= N:
        
        x = x - f_value/dfdx_value

        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))

    if store:
        return x, info
    else:
        return x, n, f_values

try:
    x0 = float(sys.argv[1])
except IndexError:
    print 'x0 must be provided at the cml'
    sys.exit(1)

def f(x):
    return sin(x)-x**5
def dfdx(x):
    return cos(x)-5*x**4

x, info = Newton(f, x0, dfdx, store=True)

for value in info:
    #print value
    print 'f(%g) = %g' % (value[0], value[1])
