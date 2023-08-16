from scitools.std import *

class ForwardEuler:
    def __init__(self, f, dt):
        self.f, self.dt = f, dt
    
    def set_initial_condition(self, u0, t0=0):
        self.u = []
        self.t = []
        
        self.u.append(float(u0))
        self.t.append(float(t0))
        self.k = 0

    def solve(self, T):
        tnew = 0
        while tnew <= T:
            unew = self.advance()
            self.u.append(unew)
            tnew = self.t[-1] + self.dt
            self.t.append(tnew)
            self.k += 1
        return array(self.u), array(self.t)

    def advance(self):
        u, dt, f, k , t = \
            self.u, self.dt, self.f, self.k, self.t[-1]
        
        unew = u[k] + dt*f(u[k], t)
        return unew

class BodyInFluid:
    def __init__(self, rho, rho_b, C_D, A, V, g=9.81):
        self.rho, self.rho_b, self.C_D, self.A, self.V, self.g = \
            rho, rho_b, C_D, A, V, g

    def __call__(self, v, t):
        rho, rho_b, C_D, A, V, g = \
            self.rho, self.rho_b, self.C_D, self.A, self.V, self.g
        return -g*(1-(rho/rho_b))-0.5*C_D*((rho*A)/(rho_b*V))*abs(v)*v
        
def test():
    problem = BodyInFluid(0.79, 1003, 0.6, 0.9, 0.08)
    T = 40
    dt = 0.1
    method = ForwardEuler(problem, dt)
    method.set_initial_condition(0)
    v, t = method.solve(T)

    plot(v, t, xlabel='t', ylabel='v')

test()
