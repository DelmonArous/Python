from numpy import *

def trapezodial_vec(f, a, x, n):
    h = (x-a)/float(n)
    xcoor = linspace(a, x, n+1)
    fx = f(xcoor)
    fx[0] /= 2.0; fx[-1] /= 2.0
    I = h*sum(fx)
    return I 

class Integral:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n

    def __call__(self, x):
        f, a, n = self.f, self.a, self.n
        return trapezoidal_vec(f, a, x, n)

G = Integral(sin, 0, 200)
value = G(2*pi)
