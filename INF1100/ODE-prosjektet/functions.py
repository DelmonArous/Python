from numpy import *
from Heaviside import H

class LinearFrictionForce:
    def __init__(self, my, R):
        self.my, self.R = my, R

    def __call__(self, dudt):
        return 6*pi*self.my*self.R*dudt

class QuadraticFrictionForce:
    def __init__(self, C_D, rho, A):
        self.C_D, self.rho, self.A = C_D, rho, A

    def __call__(self, dudt):
        return 0.5*self.C_D*self.rho*self.A*abs(dudt)*dudt

class Spring:
    def __init__(self, k):
        self.k = k

class LinearSpringForce(Spring):
    def __call__(self, u):
        return self.k*u

class SinusoidalSpringForce(Spring):
    def __call__(self, u):
        return self.k*sin(u)

class CubicSpringForce(Spring):
    def __call__(self, u):
        return self.k*(u - (1./6)*u**3)

class SinusoidalExternalForce:
    def __init__(self, F0, A, omega):
        self.F0, self.A, self.omega = F0, A, omega

    def __call__(self, t):
        return self.F0 + self.A*sin(self.omega*t)

class BumpForce:
    def __init__(self, t1, t2, F0):
        self.t1, self.t2, self.F0 = t1, t2, F0

    def __call__(self, t):
        return H(t - self.t1)*(1 - H(t - self.t2))*self.F0

class RandomForce1:
    def __init__(self, F0, A, B):
        self.F0, self.A, self.B = F0, A, B

    def __call__(self, t):
        def U(t, B):
            return random.uniform(-self.B,self.B) 
        return self.F0 + self.A*U(t, self.B)

class RandomForce2:
    def __init__(self, F0, A, my, sigma):
        self.F0, self.A, self.my, self.sigma = F0, A, my, sigma

    def __call__(self, t):
        def N(t, my, sigma):
            return random.normalvariate(self.my, self.sigma)
        return self.F0 + self.A*N(t, self.my, self.sigma)

class Zero:
    def __call__(self, u):
        return 0
