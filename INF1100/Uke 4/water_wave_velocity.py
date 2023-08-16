from scitools.std import *

def c(lmbda):
    return sqrt(((g*lmbda)/(2*pi))*(1 + (s*4*pi**2)/(rho*g*lmbda**2))*tanh(2*pi*h/lmbda))

g = 9.81
s = 7.9*10**(-4)
rho = 1*10**3
h = 50
n = 1001

lambda_small = linspace(0.001,0.1,n)
lambda_large = linspace(1,2000,n)

y1 = c(lambda_small)
y2 = c(lambda_large)

plot(lambda_small,y1, 
     xlabel='lambda',ylabel='c(lambda)',
     title='Plot of wave speed for small lambda')
figure()
plot(lambda_large,y2,
     xlabel='lambda',ylabel='c(lambda)',
     title='Plot of wave speed for large lambda')
