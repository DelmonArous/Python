from math import *

def C(x,n):
    x = float(x)
    j = 1
    term0 = 1
    term = -term0*(x**2)/(2*j*(2*j-1))
    s = term
    
    for j in range(2,n+1):
        term = -term*(x**2)/(2*j*(2*j-1))
        s += term
    
    return s

print C(0,100)
                             
