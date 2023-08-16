from scitools.std import *

def y(t):
    return v0*t - 0.5*g*t**2

g= 9.81
n = 21
v0_values = [float(v0) for v0 in sys.argv[1:]]


for v0 in v0_values:
    t = linspace(0, (2*v0/g), n)
    plot(t,y(t))
    hold('on')
    legend('v0=%g' % v0)

xlabel('time')
ylabel('height')
title('Height of ball as function of time')
