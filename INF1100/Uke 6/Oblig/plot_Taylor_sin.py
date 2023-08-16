from scitools.std import *

def S(x,n):
    s = 0
    for j in range(0,n+1):
        s += ((-1)**j)*((x**(2*j+1))/factorial(2*j+1)) 
        # All the n terms of the Taylor polynomial gets stored in s 
    return s
        
n_values = [1,2,3,6,12]   # The vaules of n for the approximations to sin(x)
x = linspace(0,4*pi,1000)
y_exact = sin(x)

plot(x,y_exact,axis=[0,4*pi,-2,2],xlabel='x',ylabel='f(x)',
     title='Plot of Taylor polynomial to sin(x)', legend='sin(x)')

hold('on')

for n in n_values:
    plot(x, S(x,n), legend='n=%d' % n)
