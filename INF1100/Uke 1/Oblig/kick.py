from math import *
    
Cd = 0.2                    # drag coefficient
g = 9.81                    # gravity
q = 1.2                     # density of the air
a = 11.0/100                # radius in meters
A = pi*(a**(2))             # cross-sectional area
m = 0.43                    # mass of the ball
Vh= 120.0/3.6               # hard kick in m/s
Vs = 10.0/3.6               # soft kick in m/s

Fdh = 0.5*Cd*q*A*(Vh)**(2)  # drag force for a hard kick
Fds = 0.5*Cd*q*A*(Vs)**(2)  # drag force for a soft kick
Fg = m*g                    # the gravity force on the ball
rh = Fdh/Fg                 # ratio for a hard kick
rs = Fds/Fg                 # ratio for a soft kick

print   '''
        The drag force on the ball for a hard kick is %.2f N
        The drag force on the ball for a soft kick is %.2f N
        The gravity force on the ball is either way %.2f N
        The ratio of the drag force for a hard kick and gravity force is %.2f
        The ratio of the drag force for a soft kick and gravity force is %.2f
        ''' % (Fdh, Fds, Fg, rh, rs)

'''
Unix> python kick.py
The drag force on the ball for a hard kick is 5.07 N
The drag force on the ball for a soft kick is 0.04 N
The gravity force on the ball is either way 4.22 N
The ratio of the drag force for a hard kick and gravity force is 1.20
The ratio of the drag force for a soft kick and gravity force is 0.01
'''
