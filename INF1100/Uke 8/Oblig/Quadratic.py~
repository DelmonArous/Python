from numpy import *

class Quadratic:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    # 1
    def value(self, x):
        return self.a*x**2 + self.b*x + self.c
    # 2    
    def table(self, L, R, n):
        print '   x      f(x)'
        print '----------------'
        x = linspace(L, R, n)  # n x values in the interval [L,R]
        for i in x:
            s = '  %s | %s' % (i, self.value(i))  # printing out the table
            print s                               # of x and f values
    # 3
    def root(self):
        if self.a == 0: # To avoid division by zero
            x0 = (-self.c/self.b)   
            return x0
        elif ((self.b)**2 - 4*self.a*self.c) < 0: # To avoid imaginary roots
            print 'There are no real roots!'
        else:
            q = sqrt((self.b)**2 - 4*self.a*self.c)
            x1 = (-self.b + q)/(2.*self.a)
            x2 = (-self.b - q)/(2.*self.a)
            return x1, x2

Q = Quadratic(a=1, b=2, c=1)
print 'Value (x = 5): ', Q.value(5)
Q.table(0,20,21)
print 'Roots (function = x**2+2*x+1): ', Q.root()

'''
Unix> python Quadratic.py
Value (x = 5):  36
   x      f(x)
----------------
  0.0 | 1.0
  1.0 | 4.0
  2.0 | 9.0
  3.0 | 16.0
  4.0 | 25.0
  5.0 | 36.0
  6.0 | 49.0
  7.0 | 64.0
  8.0 | 81.0
  9.0 | 100.0
  10.0 | 121.0
  11.0 | 144.0
  12.0 | 169.0
  13.0 | 196.0
  14.0 | 225.0
  15.0 | 256.0
  16.0 | 289.0
  17.0 | 324.0
  18.0 | 361.0
  19.0 | 400.0
  20.0 | 441.0
Roots (function = x**2+2*x+1):  (-1.0, -1.0)
'''
