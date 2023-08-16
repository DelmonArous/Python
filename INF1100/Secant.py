from numpy import *

def secant(f, x0, x1, eps=1.0E-7, store=False, N=100):
    
    f_value = f(x)
    xn_pp = x0
    xn_p = x1
    n = 2

    if store: info=[(x, f_value)]

    while abs(f_value) > eps and  n <= N:

        x = xn_p - (f(xn_p)*(xn_p - xn_pp))/(f(xn_p) - f(xn_pp))
        
        xn_p = x
        xn_pp = xn_p

        n += 1
        f_value = f(x)
        if store: info.append[(x, f_value)]

    if store:
        return x, info
    else: 
        return x, n, f_value

def eq(x):
    return sin(x)-x**5

xn, info = secant(eq,0,1,store=True)
