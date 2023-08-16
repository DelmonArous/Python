from math import *

class FuncWithDerivatives:
    def __init__(self, h = 1.0E-9):
        self.h = h

    def __call__(self, x):
        raise NotImplementedError\
            ('__call__ missing in class %s' % self.__class__.__name__)

    def df(self, x):
        h = self.h
        return ((self(x+h) - self(x-h))/2.0*h)

    def ddf(self, x):
        h = self.h 
        return ((self(x+h) - 2*self(x) + self(x-h))/(float(h)**2))

class Sine1(FuncWithDerivatives):
    def __init__(self, h = 1.0E-9):
        FuncWithDerivatives.__init__(self, h)

    def __call__(self, x):
        return sin(x)

class Sine2(FuncWithDerivatives):
    def __init__(self, h = 1.0E-9):
        FuncWithDerivatives.__init__(self, h)

    def __call__(self, x):
        return sin(x)
    
    def df(self, x):
        return cos(x)

    def ddf(self, x):
        return -sin(x)

f1 = Sine1(); f2 = Sine2()
for x in [pi/3, pi/4]:
    print 'x = %g: first-order derivative error: %g' \
        % (x, abs(f2.df(x)-f1.df(x)))
    print 'x = %g: second-order derivative error: %g' \
        % (x, abs(f2.ddf(x)-f1.ddf(x)))


