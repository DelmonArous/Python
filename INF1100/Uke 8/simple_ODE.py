from scitools.std import *

def ForwardEuler(f, dt, u0, T):

    u = []; t = []
    u.append(u0)
    t.append(0)
    n = int(round(T/dt))

    for k in range(n):
        unew = u[k] + dt*f(u[k], t[k])
        u.append(unew)
        tnew = t[-1] + dt
        t.append(tnew)
    return array(u), array(t)

def f(u, t):
    return u/10.

u0 = 0.2; dt = 1; T = 20
u, t = ForwardEuler(f, dt, u0, T)

u_exact = 0.2*exp((1/10.)*t)
plot(t, u, t, u_exact, xlabel='t', ylabel='u', 
     legend=('numerical', 'exact'), 
     title="Solution of the ODE u'=u/10, u(0)=0.2")

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

method = ForwardEuler(f, dt)
method.set_initial_condition(u0, 0)
u, t = method.solve(T)
print 'Numerical:\n', u
print 'Exact:', '\n', u_exact
