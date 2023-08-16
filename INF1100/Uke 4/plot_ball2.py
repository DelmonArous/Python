from scitools.std import *

def y(t):
    return v0*t - 0.5*g*t**2

v0_values = [float(i) for i in sys.argv[1:]]
g = 9.81; n = 100

for v0 in v0_values:
    t = linspace(0,2*v0/g,n)
    plot(t, y(t), xlabel='time (s)', ylabel='height (m)',
         legend=('v0=%g' % v0),
         title='Height of ball as function of time')
    hold('on')
    
