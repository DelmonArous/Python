from math import *

def S(t=1,n=4,alpha=0.01,T=2*pi):
    
    S = 0

    for i in range(1,n+1):
        term = (1./2*i-1)*sin(2*pi*t*(2*i-1.)/T)
        S += term
        S = S*(4/pi)
    return S
S()

