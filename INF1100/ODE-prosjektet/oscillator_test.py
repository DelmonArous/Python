from functions import *
from oscillator import *
from scitools.std import *
from scitools.misc import read_cml

def main1():

    problem = Problem()
    problem.m = 1.
    problem.initial_u = 1.
    problem.initial_dudt = 0.
    problem.friction = Zero()
    k = 1.
    problem.spring = LinearSpringForce(k)
    problem.external = Zero()
    problem.u_exact = cos
    solver = Solver()
    solver.dt = pi/20
    solver.T = 8*pi
    solver.method = ForwardEuler

    solver.solve(problem)
    visualizer = Visualizer(problem, solver)
    visualizer.visualize()

def main2():
    
    problem = Problem()
    problem.m = 5.
    problem.initial_u = 1.
    problem.initial_dudt = 0.
    my = 1./(6*pi); R = 0.1
    problem.friction = LinearFrictionForce(my, R)
    k = 1.
    problem.spring = LinearSpringForce(k)
    F0 = 0.; A = 1.; omega = 0.5
    problem.external = SinusoidalExternalForce(F0, A, omega)
    problem.u_exact = None
    solver = Solver()
    solver.method = RungeKutta4
    solver.dt = pi/80
    solver.T = 60*pi

    solver.solve(problem)
    visualizer = Visualizer(problem, solver)
    visualizer.visualize()

if __name__ == '__main__':
    if sys.argv[1] == 'main1':
        main1()
    elif sys.argv[1] == 'main2':
        main2()
    
