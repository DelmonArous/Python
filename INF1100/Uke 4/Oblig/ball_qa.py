t = float(raw_input('t=? '))
v0 = float( raw_input('v0? '))
g = 9.81

y = v0*t - 0.5*g*t**2

print 'y(%g)=%.2f m above y0 with v0=%g m/s' % (t,y,v0)

'''
Unix> python ball_qa.py 
t=? 2
v0? 15
y(2)=10.38 m above y0 with v0=15 m/s
'''
