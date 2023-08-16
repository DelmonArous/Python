from scitools.std import *

def f(x,t):
    return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

x_values = linspace(-4,4,801)
t = 0
y = f(x_values,t)

plot(x_values,y, xlabel='x',ylabel='y',
     legend='exp(-(x-3*t)^2)*sin(3*pi*(x-t))',
     title='Plot of a wave packet')
