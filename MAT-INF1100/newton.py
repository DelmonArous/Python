from math import *

def f(x):
    return sin(x)
def dfdx(x):
    return cos(x)

def newton(f,dfdx,x0):
    
    i = 0
    xp = z = x0
    abserr = abs(z)
    N = 4

    while i <= N: # and abserr >= eps*abs(z):

        z = xp - f(xp)/dfdx(xp)
        abserr = abs(z-xp)
        xp = z
        i += 1

        print 'iteration = %g: z = %.20f , absolute error = %g' % (i,z,abserr)

    return i, z

iteration, root = newton(f,dfdx,3)
