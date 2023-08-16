from numpy import *

class Line: 
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print self.__class__.__name__
        return self.c1*x + self.c0

    def table(self, L, R, n):
        s = ''
        for x in linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self, x):
        print self.__class__.__name__
        return self.c2*x**2 + Line.__call__(self, x)
    
class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3

    def __call__(self, x):
        print self.__class__.__name__
        return self.c3*x**3 + Parabola.__call__(self, x)

class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4

    def __call__(self, x):
        print self.__class__.__name__
        return self.c4*x**4 + Cubic.__call__(self, x)

c = Cubic(1, 2, 3, 4)
p = Poly4(1, 2, 3, 4, 5)
print c(2); print p(2)
