from math import *

def f(x,y):
    return (x + y)

N = 100

xpp = 0
xp = 1

for n in range(2,N):
    
    x = f(xp,xpp)
    
    print n, ': ', x

    xpp = xp
    xp = x
