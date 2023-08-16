import sys

t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81

if not 0 < t < ((2*v0)/g):
    print 'The value t=%g is out of range!' % t
    sys.exit(1)

y = v0*t - 0.5*g*t**2

print 'y(%g)=%.2f m above y0 with v0=%g m/s' % (t,y,v0)

'''
Unix> python ball_cm1_errorcheck.py -1 4
The value t=-1 is out of range
-----------------------------------------
Unix> python ball_cm1_errorcheck.py 2 20
y(2)=20.38 m above the ground with v0=20 m/s
'''
