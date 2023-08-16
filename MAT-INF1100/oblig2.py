from scitools.std import *

'''
Bruker diverse metoder for aa lose differensialligningen
x'=f(x,t)=1+x**2, x(0)=1, med steglengde h=dt til t=T
'''

def ForwardEuler(f, dt, x0, T):

    x = []; t = []
    x.append(x0)
    t.append(0)
    n = int(round(T/dt))

    for k in range(n):
        xnew = x[k] + dt*f(x[k], t[k])
        x.append(xnew)
        tnew = t[-1] + dt
        t.append(tnew)
    return array(x), array(t)

def EulerMid(f, dt, x0, T):

    x = []; t = []
    x.append(x0)
    t.append(0)
    n = int(round(T/dt))

    for k in range(n):
        xnew_h = x[k] + dt*f(x[k], t[k])/2.
        xnew = x[k] + dt*f(xnew_h, t[k] + dt/2.)
        x.append(xnew)
        tnew = t[-1] + dt
        t.append(tnew)
    return array(x), array(t)

def newMethod(f, dt, x0, T):
    x = []; t = []
    x.append(x0)
    t.append(0)
    n = int(round(T/dt))

    for k in range(n):
        xnew = (2 - dt*x[k] - 2*sqrt(1 - dt**2 - 2*x[k]*dt))/float(dt)
        x.append(xnew)
        tnew = t[-1] + dt
        t.append(tnew)
    return array(x), array(t)

def f(x, t):
    return x**2+1

x0 = 1; dt = 0.1; T = 0.6
x_Euler, t = ForwardEuler(f, dt, x0, T)
x_EulerMid, t = EulerMid(f, dt, x0, T)
x_newMethod, t = newMethod(f, dt, x0, T)
x_exact = tan(t+(pi/4))

plot(t, x_Euler,'s-', t, x_exact, 
     t, x_EulerMid,'v-', t, x_newMethod,'d-',
     xlabel='t', ylabel='x',
     axis=[0,0.6,min(x_exact),max(x_exact)],
     legend=("Euler's method", "Exact", "Euler's midpoint", "New method"), 
     title="Solution of the ODE x'=x**2+1, x(0)=1",
     hardcopy='Oblig2.ps') 

print x_Euler
print x_EulerMid
print x_newMethod
print x_exact

'''
### Her ser vi Eulers midtpunktmetode vil da gi en bedre tilnearming (mindre feil) 
    enn resten av metodene for store verdier av T ###

Euler:
[ 1.          1.2         1.444       1.7525136   2.15964399  2.72605021
  3.56918518]
---------------------------------------------------------------
EulerMid:
[ 1.          1.221       1.50204834  1.87922282  2.42266082  3.28780562
  4.89191811]
---------------------------------------------------------------
NewMethod:
[ 1.          1.22361117  1.51049451  1.90154482  2.48191221  3.46650343
  5.63947409]
---------------------------------------------------------------
Exact:
[ 1.          1.22304888  1.50849765  1.89576512  2.46496276  3.40822344
  5.33185522]
'''
