from scitools.std import *

#Constants
m1 = 6.4*10**23       # mass of Mars
m2 = 1000.0           # mass of Mars Express
radius = 3400.0*1000  # radius of Mars
G = 6.67428*10**-11   # gravitational constant
n = 10**5             # number of calculations
dt = 1                # timestep

#Calculation of gravitational force on the bodies  
def grav_force(x1,x2,y1,y2):
    a = abs(x2-x1)                    # displacement x-direction 
    b = abs(y2-y1)                    # displacement y-direction 
    r = sqrt((x2-x1)**2 + (y2-y1)**2) # distance between the bodies
    F = float(G*m1*m2)/r**2           # abs. grav. force on each body
    theta = arctan(float(b)/a)        # angle between x-axis and r-direction

    if x1<x2:
        F_x1 = F*cos(theta)
        F_x2 = -F*cos(theta)
    else:
        F_x1 = -F*cos(theta)
        F_x2 = F*cos(theta)
    if y1<y2:
        F_y1 = F*sin(theta)
        F_y2 = -F*sin(theta)
    else:
        F_y1 = -F*sin(theta)
        F_y2 = F*sin(theta)

    return F_x1,F_x2,F_y1,F_y2

# Declaring arrays with initial values
t = zeros(n, float)
x1 = zeros(n, float)
y1 = zeros(n, float)
x2 = zeros(n, float)
y2 = zeros(n, float)

x1[0] = 0; y1[0] = 0
x2[0] = (10107+3400)*1000; y2[0] = 0
 
v_x1 = zeros(n, float)
v_y1 = zeros(n, float)
v_x2 = zeros(n, float)
v_y2 = zeros(n, float)

v_x1[0] = 0; v_y1[0] = 0
v_x2[0] = 0; v_y2[0] = 1166

#Calculations
teller = range(n-1)
for i in teller:
    F_x1,F_x2,F_y1,F_y2 = grav_force(x1[i],x2[i],y1[i],y2[i])
    
    v_x2[i+1] = v_x2[i] + dt*F_x2/m2
    v_y2[i+1] = v_y2[i] + dt*F_y2/m2
    
    x2[i+1] = x2[i] + dt*v_x2[i+1]
    y2[i+1] = y2[i] + dt*v_y2[i+1]
    
    t[i+1] = t[i] + dt

theta1 = linspace(0,2*pi,n)
x = radius*cos(theta1)
y = radius*sin(theta1)

plot(x,y, x2,y2,
     xlabel='x-axis [m]', ylabel='y-axis [m]',
     legend=("Mars","Mars Express' orbit"),
     title='Plot of the trajectory of Mars Express')

raw_input('Press Enter: ')
