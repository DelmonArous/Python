from ODESolver import RungeKutta4, ForwardEuler
from numpy import *

def _f1(u, t):
    return u/2.

u0 = 1; dt = 0.5; T = 6;

for Method_class in ForwardEuler, RungeKutta4:
    method = Method_class(_f1, dt)
    method.set_initial_condition(u0)
    u, t = method.solve(T)
    print Method_class.__name__, ':\n', u
