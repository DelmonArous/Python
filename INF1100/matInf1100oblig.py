from math import *

def f(x,y):

    return (3*x - y)

N = 800

xp = (3 - sqrt(5)) / 2.
xpp =  1

for n in range(2,N+1):
     
    x = f(xp,xpp)
    
    print 'n =',n, ': ', x

    xpp = xp
    xp = x

'''
Unix> python matInf1100oblig.py
       :
       :
n = 15 :  5.37445302484e-07
n = 16 :  2.0518477406e-07
n = 17 :  7.81090196966e-08
n = 18 :  2.91422850296e-08
n = 19 :  9.31783539215e-09
n = 20 :  -1.18877885313e-09
n = 21 :  -1.28841719516e-08
       :
       :
n = 776 :  -5.42377465889e+307
n = 777 :  -1.41996264043e+308
n = 778 :  -inf
n = 779 :  -inf
n = 780 :  nan
n = 781 :  nan
n = 782 :  nan
n = 783 :  nan
        :
        :
'''

