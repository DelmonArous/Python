import numpy as np
import matplotlib.pyplot as plt
import sys

N = int(sys.argv[1]) #number of terms in the sum

#Discretization
n = 120 #number of points including endpoints.
x = np.linspace(0,1,n)

#Given function
def f(x):
    return x

#Computing Fourier coefficients. 
c_1 = np.empty(N) #Fourier sine series. Note c_k = c[k-1]
c_2 = np.empty(N+1) #Fourier cosine series. c_k = c[k]
for i in range(N):
    c_1[i] = 2*np.trapz(f(x)*np.sin(float(i+1)*np.pi*x),x)
for i in range(N+1):
    c_2[i] = 2*np.trapz(f(x)*np.cos(float(i)*np.pi*x),x)
c_2[0] = c_2[0]/2. #c_0 should be divided by 2

print 'Coefficients: '
print 'sine: ', c_1
print 'cosine: ', c_2

#Computing series
k= np.arange(1,N+1,1.)
x = np.linspace(-3.,3.,200) #Plotting range
X,K = np.meshgrid(x,k)
g_1 = np.dot(np.transpose(c_1),np.sin(K*np.pi*X)) #Fourier sine series

k= np.arange(0,N+1,1.) #Need to include c_0 in the cosine series
X,K = np.meshgrid(x,k)
g_2 = np.dot(np.transpose(c_2),np.cos(K*np.pi*X)) #Fourier cosine series

#Plotting
plt.plot(x,g_1, label='Sine series')
plt.plot(x,g_2, label='Cosine series')
plt.plot(x,f(x), '--', label='f(x) = x')
legend = plt.legend(loc='upper left')
plt.show()
