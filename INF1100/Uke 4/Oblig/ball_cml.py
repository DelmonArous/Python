import sys

t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81

y = v0*t - 0.5*g*t**2

print 'y(%g)=%.2f m above y0 with v0=%g m/s' % (t,y,v0)

'''
Unix> python ball_cm1.py 2 15
y(2)=10.38 m above y0 with v0=15 m/s
'''
