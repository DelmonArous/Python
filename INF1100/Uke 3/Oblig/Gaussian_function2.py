from math import *

def gauss(x, m=0.0, s=1.0):
    
        f = 1.0/(sqrt(2*pi)*s)*exp(-0.5*((x - m)/s)**(2.0)) 
        
        return f

print '   x     gauss(x)'

for x in range(-5,6,1):
    print '%4d %10.4f ' % (x,gauss(x))

'''
Unix> python Gaussian_function2.py
   x     gauss(x)
  -5     0.0000 
  -4     0.0001 
  -3     0.0044 
  -2     0.0540 
  -1     0.2420 
   0     0.3989 
   1     0.2420 
   2     0.0540 
   3     0.0044 
   4     0.0001 
   5     0.0000 
'''
