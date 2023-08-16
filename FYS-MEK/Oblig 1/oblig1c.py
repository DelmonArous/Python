from scitools.std import *

dt = 0.01; my = 0.1; g = 9.81; T = 6.; v0 = 5. 
n = int(round(T/dt))
t = zeros(n); v = zeros(n); a = zeros(n)
v[0] = v0
a = a + -my*g

for i in range(n-1):
    v[i+1] = v[i] + dt*a[i]
    t[i+1] = t[i] + dt

v_exact = -my*g*t + v0

plot(t, v, t, v_exact, legend=('v(t) numerical', 'v(t) exact'), 
     title='Plot of v(t) and comparison with the analytical solution', 
     xlabel='t[s]', ylabel='v[m/s]')
