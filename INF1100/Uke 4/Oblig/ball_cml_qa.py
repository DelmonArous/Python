import sys

try:
    t = float(sys.argv[1])
except IndexError:
    print 'You failed to provide the command-line argument t'
    t = float(raw_input('t=? '))
try:
    v0 = float(sys.argv[2])
except IndexError:
    print 'You failed to provide the command-line argument v0'
    v0 = float(raw_input('v0=? '))

g = 9.81
y = v0*t - 0.5*g*t**2

print 'y(%g)=%.2f m above y0 with v0=%g m/s' % (t,y,v0)

'''
Unix> python python ball_cm1_qa.py
You failed to provide the command-line argument t
t=? 2
You failed to provide the command-line argument v0
v0=? 15
y(2)=10.38 m above y0 with v0=15 m/s
-------------------------------
Unix> python ball_cm1_qa.py 2
You failed to provide the command-line argument v0
v0=? 15
y(2)=10.38 m above y0 with v0=15 m/s
'''
