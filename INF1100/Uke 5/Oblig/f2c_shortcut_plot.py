from scitools.std import *

def C_exact(F):
    return (5./9)*(F - 32)

def C_approx(F):
    return (F - 30)/2.

F = linspace(-20,120,280)
C1 = C_exact(F)
C2 = c_approx(F)

plot(F, C1, F, C2, xlabel='Fahrenheit', ylabel='Celsius',
     legend=('C', 'C~'),
     title='Comparison between C and C~')
