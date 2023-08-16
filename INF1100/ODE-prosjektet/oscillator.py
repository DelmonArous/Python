from scitools.misc import *
from scitools.std import *
from wavelength import *
from ODESolver import *

class Problem:
    def initialize(self):
        self.m = eval(read_cml('--m', 1.0))
        self.initial_u = eval(read_cml('--initial_u', 1.0))
        self.initial_dudt = eval(read_cml('--initial_dudt', 0.0))
        s = read_cml('--friction', '0')
        self.friction = StringFunction(s, independent_variable='dudt')
        s = read_cml('--spring', 'u')
        self.spring = StringFunction(s, independent_variable='u')
        s = read_cml('--external', '0')
        self.external = StringFunction(s, independent_variable='t')
        s = read_cml('--u_exact', '0')
        if s != '0':
            self.u_exact = \
                StringFunction(s, independent_variable='t')
            self.u_exact.vectorize(globals())
        else:
            self.u_exact = None
            
    def rhs(self, u, t):
        m, f, s, F = \
            self.m, self.friction, self.spring, self.external
        u, dudt = u
        return [dudt, (1./m)*(F(t) - f(dudt) - s(u))]

class Solver:
    def initialize(self):
        self.T = eval(read_cml('--T', 4*pi))
        self.dt = eval(read_cml('--dt', pi/20))
        self.method = eval(read_cml('--method', 'RungeKutta4'))

    def solve(self, problem):
        self.solver = self.method(problem.rhs, self.dt)
        ic = [problem.initial_u, problem.initial_dudt]
        self.solver.set_initial_condition(ic, 0.0)
        self.u, self.t = self.solver.solve(self.T)

class Visualizer:
    def __init__(self, problem, solver):
        self.problem = problem
        self.solver = solver

    def visualize(self):
        t = self.solver.t
        u, dudt = self.solver.u[:,0], self.solver.u[:,1]
        K = 0.5*self.problem.m*dudt**2
        peaks_min, peaks_max = minmax(t, u)
        wavelength_max = wavelength(peaks_max)

        title = 'solver=%s, dt=%g, m=%g' % \
            (self.solver.method, self.solver.dt, self.problem.m)

        if isinstance(self.problem.friction, StringFunction):
            title += ' f=%s' % str(self.problem.friction)
        if isinstance(self.problem.spring, StringFunction):
            title += ' s=%s' % str(self.problem.spring)
        if isinstance(self.problem.external, StringFunction):
            title += ' F=%s' % str(self.problem.external)
            
        plot_type= ''
        while plot_type != 'quit':
            plot_type = raw_input('Specify a plot: ')
            figure()
            if plot_type == 'u':
                plot(t, u, xlabel='t', ylabel='u',
                     legend='u numerical',title=title)
                if self.problem.u_exact is not None:
                    hold('on')
                    plot(t, self.problem.u_exact(t),
                         legend='exact')
                show()
                hardcopy('tmp_u.eps')
            elif plot_type == 'dudt':
                plot(t, dudt, xlabel='t', ylabel='u',
                     legend='dudt numerical',title=title)
            elif plot_type == 'dudt-u':
                plot(u, dudt, xlabel='t',ylabel='u',
                     legend='u versus dudt',title=title)
            elif plot_type == 'K':
                plot(t, K, xlabel='t', ylabel='u',
                     legend='Kinetic energy',title=title)
            elif plot_type == 'wavelength':
                plot(range(len(wavelength_max)), wavelength_max,
                     xlabel='indices', ylabel='wavelength',
                     legend='Wavelength',title=title)

def main():
    problem = Problem()
    problem.initialize()
    solver = Solver()
    solver.initialize()
    solver.solve(problem)
    visualizer = Visualizer(problem, solver)
    visualizer.visualize()

if __name__== '__main__':
    main()
