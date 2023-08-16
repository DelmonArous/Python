from scitools.std import *

def g(x):
    return (x**6)*sin(pi*x)

def dg(x):
    return ((6*x**5)*sin(pi*x) + (pi*x**6)*cos(pi*x))

def Newton_plot(f, x, dfdx, eps=1E-7):
    
    f_value = f(x)
    N = 100; n = 0
    info = [(x, f_value)]

    while abs(f_value) > eps and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g)=%g" % \
                                 (x, dfdx_value))
        
        x = x - f_value/dfdx_value
        f_value = f(x)
        
        info.append((x, f_value))
        n += 1

    return x, info

x0_values = [-2.6,-1.2,0.6,1.5,1.7]

for x0 in x0_values:
    x, info = Newton_plot(g ,x0, dg, eps=1E-13)
    print 'Root: ', x
    for i in range(len(info)):
        print 'Iteration %3d: f(%g)=%g' % \
            (i,info[i][0], info[i][1])
