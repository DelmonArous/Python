from numpy import *

class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' % \
                                      self.__class__.__name__)

    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

class MC(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        h = float(b-a)/n
        x = random.uniform(a, b, n)
        w = zeros(len(x)) + h
        return x, w

def f(x): 
    return 1 + 2*x
mc = MC(0, 1, 101)
print mc.integrate(f)
