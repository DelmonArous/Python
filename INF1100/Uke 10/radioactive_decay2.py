from scitools.std import *
from ODESolver import RungeKutta4

class Decay2:
    def __init__(self, tau_A, tau_B):
        self.tau_A, self.tau_B = tau_A, tau_B

    def __call__(self, u, t):
        tau_A, tau_B = self.tau_A, self.tau_B
        u_A = u[1]/float(tau_B) - u[0]/float(tau_A)
        u_B = u[0]/float(tau_A) - u[1]/float(tau_B)
        return [u_A, u_B]

u_init = [1, 1]; T = 30; dt = 1./6; tau_A = 8; tau_B = 40
f = Decay2(tau_A, tau_B)

method = RungeKutta4(f, dt)
method.set_initial_condition(u_init) 
u, t = method.solve(T)
u_A = u[:, 0]; u_B = u[:, 1]
print method.__class__.__name__, ':\n', u
plot(t, u_A, t, u_B,
     hold='on', legend=('u_A', 'u_B'),
     title=('Solved the two coupled ODEs problems using %s method' \
         % (method.__class__.__name__)))
