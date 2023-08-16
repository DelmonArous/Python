import sys

g = 9.81
t = float(sys.argv[1])
v0 = float(sys.argv[2])

if not 0 < t < ((2*v0)/g):
    raise ValueError('The value t=%g is out of range. '\
                     'The legal interval for t is [0,%.1f]' % (t,2*v0/g))

y = v0*t - 0.5*g*t**2

print 'y(%g)=%.2f m above y0 with v0=%g m/s' % (t,y,v0)

'''
Unix> python ball_cm1_ValueError.py -1 20
Traceback (most recent call last):
  File "ball_cm1_ValueError.py", line 18, in <module>
    'The legal interval for t is [0,%.1f]' % (t,2*v0/g))
ValueError: The value t=-1 is out of range. The legal interval for t is [0,4.1]
'''
