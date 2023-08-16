v0 = 5
t = 0
g = 9.81
T = 2*v0/g
dt = T/10.0

print ' t       y(t)'

while t <= T:
    y = v0*t - (1./2)*g*t**2
    print '%.2f %7.3f m' % (t,y)
    t += dt
