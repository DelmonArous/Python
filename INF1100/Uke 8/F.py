from math import *

class F2:
    def __init__(self, a, w):
        self.a = a
        self.w = w
        
    def __call__(self, x):
        return exp(-self.a*x)*sin(self.w*x)

f = F2(1.0, 0.1)
print f(pi)
f.a = 2
print f(pi)
