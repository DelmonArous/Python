from math import *

def f(x,y,z):
    
    return (x + y + z)

N = 100

xppp = 0
xpp = 1
xp =  1

for n in range(3,N+1):
     
    x = f(xppp,xpp,xp)
    
    print 'n =',n, ': ', x

    xppp = xpp
    xpp = xp
    xp = x
