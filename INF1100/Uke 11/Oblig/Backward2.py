from math import *

class Diff:
    def __init__(self, f, h = 1E-9):
        self.f, self.h = f, float(h)

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x)-f(x-h))/float(h)

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h) - 4*f(x-h) + 3*f(x))/(2.*h)

h_values = [2**(-k) for k in range(0,15)];
t = 0
def g(t): return exp(-t)
def dg(t): return -exp(-t)

for h in h_values:
    approx1 = Backward1(g, h)
    approx2 = Backward2(g, h)
    print 'h = %.2E: Backward1: %g, Backward2: %g' \
        % (h, approx1(t), approx2(t))
    print 'Error in derivative with Backward1 method is', (abs(dg(t) - approx1(t)))
    print 'Error in derivative with Backward2 method is', (abs(dg(t) - approx2(t)))
    print '------------'
