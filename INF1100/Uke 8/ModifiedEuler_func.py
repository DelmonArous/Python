from scitools.std import *

def EulerMidpoint_method(f, dt, u0, T, N):

    u = []; t = []
    u.append(u0)
    t.append(0)
    n = int(round(T/dt))      

    for k in range(n):
        tnew = t[-1] + dt
        t.append(tnew)
        v = [0]*N
        v[0] = u[k]
        for q in range(1, N+1):
            v[q] = u[k] + 0.5*dt*(f(v[q-1], t[k+1]) + f(u[k],t[k]))
        unew = v[N]
        u.append(unew)
            
    return array(u), array(t)

class ModifiedEuler:
    def __init__(self, f, dt, N):
        self.f, self. dt, self.N = f, dt, N
        
    def set_initial_condition(self, u0, t0=0):
        self.u = []
        self.t = []

        self.u.append(u0)
        self.t.append(t0)
        self.k = 0
        self.q = 1

    def solve(self, T):
        u, t, f, dt, N, k, q = \
            self.u, self.t, self.f, self.dt, self.N, self.k, self.q
        tnew = 0
        self.v = [0]*(N+1)
        while tnew <= T:
            tnew = t[-1] + dt
            t.append(tnew)
            while q <= N:
                self.v[q] = \
                    u[k] + 0.5*dt*(f(self.v[q-1], t[k+1]) + f(u[k],t[k]))
                q += 1
            unew = self.advance()
            u.append(unew)
            k += 1

        return array(self.u), array(self.t)
    
    def advance(self):
        u, dt, f, k , t, q, N = \
            self.u, self.dt, self.f, self.k, self.t[-1], self.q, self.N
        
        unew = self.v[N]
        return unew

def _test():
    def f(u, t):
        return -2.*u
    
    dt = 0.1
    N = 4
    method = ModifiedEuler(f, dt, N)
    method.set_initial_condition(1)
    T = 1.5
    u, t = method.solve(T)

    plot(t, u)

_test()
