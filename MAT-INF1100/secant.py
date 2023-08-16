from math import *

def f(x):
    return (x-1)**3

def secant(f,x0,x1,eps=1E-17):
    
    i = 0
    xpp = x0
    xp = z = x1
    abserr = abs(z)
    N = 6

    while i <= N and abserr >= eps*abs(z):

        z = xp - f(xp)*(xp-xpp)/(f(xp)-f(xpp))
        abserr = abs(z-xp)
        relerr = abs(z-xp)/abs(z)
        xpp = xp
        xp = z
        i += 1

        print 'iteration = %g: z = %.20f , absolute error = %g, relative error = %g' % (i,z,abserr,relerr)

    return i, z

iteration, root = secant(f,0.5,1.2)

        
