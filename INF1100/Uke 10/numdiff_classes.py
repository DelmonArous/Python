class Superclass:
    def __init__(self, f, h=1E-9):
        self.f, self. h = f, float(h)

class Backward(Superclass):
    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x-h))/float(h)

class Derivative(Superclass):
    def __class__(self, x):
        h, f = self.h, self.f
        return (f(x+h) - f(x))/float(h)

class Central(Superclass):
    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x+h)-f(x-h))/(2*h)
