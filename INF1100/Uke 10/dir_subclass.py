from numpy import *

class Line: 
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return self.c1*x + self.c0

    def table(self, L, R, n):
        s = ''
        for x in linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Parabola0(Line):
    pass

l = Line(1, 2)
p = Parabola0(1, 2)
print dir(l); print dir(p)
