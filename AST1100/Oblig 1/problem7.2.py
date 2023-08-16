from scitools.std import *

# Constants
m1 = 6.4*10**23       # mass of Mars [kg]
m2 = 100.0            # mass of Beagle 2 [kg]
radius = 3400.0*1000  # radius of Mars [m]
G = 6.67428*10**-11   # gravitational constant [N*(m/kg)**2]
k = 0.00016           # friction constant [kg/s]
n = 10**5             # number of calculations
dt = 1                # timestep [s]

# Calculation of gravitational force on the bodies  
def g_force(x1,x2,y1,y2):
    a = abs(x2-x1)                    # displacement x-direction 
    b = abs(y2-y1)                    # displacement y-direction 
    r = sqrt((x2-x1)**2 + (y2-y1)**2) # distance between the bodies
    F = (G*m1*m2)/r**2                # abs. grav. force on each body
    theta = arctan(float(b)/a)        # angle between x-axis and r-direction

    # giving correct positive/negative-sign 
    # according to the position of Beagle 2 relative to Mars
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

def f_force(v_x2,v_y2):
    v = sqrt(v_x2**2 + v_y2**2)      # velocity of body
    f = -k*v                         # abs. fric. force
    theta = arctan(float(v_x2)/v_y2) # angle between x-axis and velocity
    f_x = abs(f*cos(theta))          # x-component
    f_y = abs(f*sin(theta))          # y-component

    # giving correct positive/negative-sign
    if v_x2 > 0:
        f_x = -f_x
    if v_y2 > 0:
        f_y = -f_y

    return f_x,f_y

# Declaring lists with initial values
t = [0]
x1 = [0]; y1 = [0]
x2 = [(-298-3400)*1000]; y2 = [0] 
v_x1 = [0]; v_y1 = [0]
v_x2 = [0]; v_y2 = [-4000]

#Calculations using Euler-Cromer
i = 0       # loop counter
land = 'no' # variable with value equal to 'no'
while land=='no' and i<(n-2):
    F_x1,F_x2,F_y1,F_y2 = g_force(x1[i],x2[i],y1[i],y2[i])
    f_x,f_y = f_force(v_x2[i],v_y2[i])

    v_x1.append(v_x1[i] + dt*F_x1/m1)
    v_x2.append(v_x2[i] + dt*(F_x2 + f_x)/m2)
    v_y1.append(v_y1[i] + dt*F_y1/m1)
    v_y2.append(v_y2[i] + dt*(F_y2 + f_y)/m2)
    
    x1.append(x1[i] + dt*v_x1[i+1])
    x2.append(x2[i] + dt*v_x2[i+1])
    y1.append(y1[i] + dt*v_y1[i+1])
    y2.append(y2[i] + dt*v_y2[i+1])
    
    t.append(t[i] + dt)
    
    if sqrt(x2[i]**2+y2[i]**2)<=radius:
        land = 'yes' # the loop stops
    
    i = i + 1

# Transforming lists into arrays to plot the solution
x2 = array(x2)       
y2 = array(y2)

# Surface approximation of Mars
theta = linspace(0,2*pi,n)
x = radius*cos(theta)
y = radius*sin(theta)

plot(x,y, x2,y2,
     xlabel='x-axis [m]', ylabel='y-axis [m]',
     axis='equal',legend=("Mars","Beagle 2's orbit"),
     title='Plot of the trajectory of Beagle 2')

raw_input('Press Enter: ')
