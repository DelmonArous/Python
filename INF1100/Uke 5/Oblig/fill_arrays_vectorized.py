from numpy import *

def h(x):
    return (1/sqrt(2*pi))*exp(-0.5*x**2)

x_values = linspace(-4,4,9)
h_array = h(x_values)

print x_values
print h_array

'''
Unix> python fill_arrays_vectorized.py
[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
[  1.33830226e-04   4.43184841e-03   5.39909665e-02   2.41970725e-01
   3.98942280e-01   2.41970725e-01   5.39909665e-02   4.43184841e-03
   1.33830226e-04]
'''
