from scitools.std import *

g = 9.81

try:
    m = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    m = float(raw_input('m? '))
    v0 = float(raw_input('v0? '))

def y(t):
    return v0*t - 0.5*g*t**2
def v(t):
    return v0 - g*t
def P(t):
    return m*g*y
def K(t):
    return 0.5*m*v**2

t = linspace(0,(2*v0/g), 1000)
y = y(t); v = v(t); p = P(t); k = K(t)

plot(t, p, t, k, t, (p+k), xlabel='seconds', ylabel='joule',
     legend=('Potential energy','Kinetic energy','P(t)+K(t)'),
     title='Plot of potential and kinetic energy',
     axis=[t[0],t[-1],0,max(p+k)])
