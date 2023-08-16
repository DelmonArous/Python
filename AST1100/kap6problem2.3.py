from scitools.std import *

def delta(x):
    delta = ((x*exp(x)/(exp(x)-1)) - 5)**2
    
    return delta

x = linspace(1,10,1000)
delta = delta(x)
delta_best = delta[0]
x_best = 5.5

for i in range(len(x)):
    if delta[i] < delta_best:
        delta_best = delta[i]
        x_best = x[i]
        
print x_best


plot(x,delta)

raw_input('Enter:')
