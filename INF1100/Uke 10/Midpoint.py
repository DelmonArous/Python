from scitools.std import *

class ODESolver:
    def __init__(self, f, dt):
        self.f = f
        self.dt = dt

    def advance(self):
        raise NotImplementedError

    def set_initial_condition(self, u0, t0=0):
        self.u = []    
        self.t = []    
        
        self.u.append(asarray(u0, float))
        self.t.append(float(t0))
        self.k = 0  

    def solve(self, T):
        self.k = 0
        tnew = 0
        while tnew <= T:
            unew = self.advance()
            self.u.append(unew)
            tnew = self.t[-1] + self.dt
            self.t.append(tnew)
            self.k += 1
        return array(self.u), array(self.t)
    
class ForwardEuler(ODESolver):
    def advance(self):
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]

        unew = u[k] + dt*f(u[k], t)
        return unew

class RungeKutta4(ODESolver):
    def advance(self):
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t[-1]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t)
        K2 = dt*f(u[k] + 0.5*K1, t + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t + dt2)
        K4 = dt*f(u[k] + K3, t + dt)
        unew = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return unew

class MidpointMethod(ODESolver):
    def advance(self):
        u, dt, f, k , t = \
            self.u, self.dt, self.f, self.k, self.t[-1]
        unew = u[k-1] + 2*dt*f(u[k], t)
        return unew

u0 = 1; dt = 0.5; T = 0.5*10
def f(u, t):
    return u

for Method in ForwardEuler, RungeKutta4, MidpointMethod:
    method = Method(f, dt)
    method.set_initial_condition(u0)
    u, t = method.solve(T)
    print Method.__name__, ':\n', u
    plot(t, u, hold='on', legend=('%s' % Method.__name__))

t = linspace(0, T, 11)
plot(t, exp(t), legend='exact')
