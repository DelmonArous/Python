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

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2

    def __call__(self, x):
        return self.c2*x**2 + Line.__call__(self, x)

class SinePlusQuadratic(Parabola):
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, c, b, a)
        self.A, self.w = A, w
    
    def __call__(self, x):
        return self.A*sin(self.w*x) + Parabola.__call__(self, x)

a = SinePlusQuadratic(5, pi/2, 2, -5, 3)
print a.table(3, 5, 10)
        
