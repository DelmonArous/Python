from scitools.std import *

def v(r):
    return (((B/2*my)**(1./n))*(n/n+1)*(R**(1+(1./n)) - r**(1+(1./n))))

R = 1; B = 0.02; my = 0.02
n_values = linspace(1, 0.01, 101)
r = linspace(0, R, 1001)

for n in n_values:
    y = (v(r)/v(0))
    plot(r, y, axis=[r[0], r[-1], 0, 1],
         xlabel='r', ylabel='v(r)')
    
