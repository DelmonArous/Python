from scitools.std import *
from ODESolver import *
import glob, os, time

for filename in glob.glob('osc*.png'):
    os.remove(filename)

u_init = [1, 0]; dt = pi/20; T = 6*pi; m = 1.;
dt_values = [pi/(i+1) for i in range(21)]

def friction(dudt): return 0
def spring(u): return u
def external(t): return 0

def rhs(u, t):
    u0, u1 = u
    return [u1, (1/m)*(external(t) - friction(u1) - spring(u0))]

for Method_class in ForwardEuler, RungeKutta4:
    method = Method_class(rhs, dt)
    method.set_initial_condition(u_init)
    u, t = method.solve(T)
    
    u0_values = u[:, 0]
    u1_values = u[:, 1]
    u_exact = cos(t)

    K = 0.5*m*u1_values**2
    P = 0.5*m*u0_values**2
    analytical_solution = 0.5*m*(cos(t))**2 + 0.5*m*(sin(t))**2

    figure()
    plot(t, u0_values, t, u1_values, t, u_exact, u0_values, u1_values,
         xlabel='t', ylabel='u',
         title=('Solved the system of ODEs using %s method' \
                    % Method_class.__name__),
         legend=("u0","u1","exact", "u' versus u"))
    figure()
    plot(t, K, t, P, t, (K+P), t, analytical_solution,
         xlabel='t', ylabel='u',
         legend=('Kinetic energy','Potensial energy',
                 'Kinetic+Potensial','Analytical solution'),
         title=('Plot of kinetic and potensial energy using %s' \
                    % Method_class.__name__))

'''
counter = 0
for dt in dt_values:
    method = ForwardEuler(rhs, dt)
    method.set_initial_condition(u_init)
    u, t = method.solve(T)

    u0_values = u[:, 0]
    u1_values = u[:, 1]
    u_exact = cos(t)

    figure()
    plot(t, u0_values, t, u1_values, t, u_exact, u0_values, u1_values,
         xlabel='t', ylabel='u', axis=[-5, 20, -5, 6],
         title='Solved the system of ODEs using ForwardEuler method',
         legend=("u0","u1","exact", "u' versus u"),
         hardcopy='osc%04d.png' % counter)
    counter += 1
    time.sleep(0.7)

movie('osc*.png', encoder='convert', output_file='oscmovie.gif')
'''
