from scitools.std import *
from ODESolver import *
import getopt, sys

class RHS:
    def __init__(self, friction, spring, external, m):
        self.friction, self.spring, self.external, self.m = \
            friction, spring, external, m

    def __call__(self, u, t):
        u0, u1 = u
        m = self.m
        return [u1,(1./m)*(self.external(t)-self.friction(u1)-self.spring(u0))]

def solve(T, dt, initial_u, initial_dudt, method=RungeKutta4, m=1.0,
          friction=lambda dudt: 0, spring=lambda u: u, external=lambda t: 0):

    f = RHS(friction, spring, external, m)

    use_method = method(f, dt)
    use_method.set_initial_condition([initial_u, initial_dudt])
    u, t = use_method.solve(T)

    return u, t 

def makeplot(T, dt, initial_u, initial_dudt, method=RungeKutta4, m=1.0,
             friction=lambda dudt: 0, spring=lambda u: u, external=lambda t: 0,
             u_exact=None):
    
    u, t = solve(T, dt, initial_u, initial_dudt, method, m, friction, spring, external)
    
    u0_values = u[:, 0]
    u1_values = u[:, 1]
    
    if u_exact is not None:
        u_exact = cos(t)
        plot(t, u0_values, t, u1_values, t, u_exact, u0_values, u1_values,
             xlabel='t', ylabel='u', legend=("u0","u1","exact","u' versus u"), 
             title = ('Solved the ODEs using %s method' % method.__name__))
    else:
        plot(t, u0_values, t, u1_values, u0_values, u1_values,
             xlabel='t', ylabel='u', legend=("u0","u1","u' versus u"),
             title = ('Solve the ODEs using %s method' % method.__name__))

def get_input():
    options, args = getopt.getopt(sys.argv[1:], '', 
                                  ['T=','dt=','initial_u=','initial_dudt=','m=',
                                  'method=','friction=','spring=','external=','u_exact='])
    T = 5*pi
    dt = pi/20
    m = 1.
    initial_u = 1; initial_dudt = 0
    method = ForwardEuler
    friction = lambda dudt: 0
    spring = lambda u: u
    external = lambda t: 0
    u_exact = None

    for option, value in options:
        if option == '--T':
            T = eval(value)
        elif option == '--dt':
            dt = eval(value)
        elif option == '--initial_u':
            initial_u = eval(value)
        elif option == '--initial_dudt':
            initial_dudt = eval(value)
        elif option == '--m':
            m = eval(value)
        elif option == '--method':
            method = eval(value)
        elif option == '--friction':
            friction = StringFunction(value, independent_variable='dudt')
        elif option == '--spring':
            spring = StringFunction(value, independent_variable='u')
        elif option == '--external':
            external = StringFunction(value, independent_variable='t')
        elif option == '--u_exact':
            u_exact = StringFunction(value, independent_variable='t')
            u_exact.vectorize(globals())
        
    return makeplot(T, dt, initial_u, initial_dudt, method, m,
                    friction, spring, external, u_exact)

if __name__== '__main__':
    get_input()
