import numpy as np
import matplotlib.pyplot as plt
import sys

#Discretization (Give number n as argument)
n = int(sys.argv[1])
h = 1./float(n+1)
x = np.linspace(h,1-h,n)

#Defining f
def f(x):
    z = np.empty(x.size)
    for i in range(0,x.size):
        if(x[i] <= 0.5):
            z[i] = x[i]
        else:
            z[i] = 1.-x[i]
    return z


#Computing fourier coefficients c
k= np.arange(1,n+1,1.)
X,K = np.meshgrid(x,k)
T = np.sin(K*np.pi*X)
c = 2.*h*np.dot(T,f(x))

#Computing f and g for plot:
x = np.linspace(0,1,120)
X,K = np.meshgrid(x,k)
g = np.dot(np.transpose(c),np.sin(K*np.pi*X))

#Plotting
plt.plot(x,g)
plt.plot(x,f(x), '--')
plt.show()
    

