from numpy import *

def h(x):
    return (1/sqrt(2*pi))*exp(-0.5*x**2)

x_values = [x for x in range(-4,5,1)]
x_array = zeros(len(x_values))
h_array = zeros(len(x_values))

for x in range(len(x_values)):
    h_array[x] = h(x_values[x])
    x_array[x] = x_values[x]

print x_array
print h_array

'''
Unix> python fill_array_loop.py
[-4. -3. -2. -1.  0.  1.  2.  3.  4.]
[  1.33830226e-04   4.43184841e-03   5.39909665e-02   2.41970725e-01
   3.98942280e-01   2.41970725e-01   5.39909665e-02   4.43184841e-03
   1.33830226e-04]
'''

