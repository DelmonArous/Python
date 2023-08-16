from scitools.std import *

#Constants
m1 = 6.42*10**23
m2 = 2.*10**30
m3 = 8.*10**30
AU = 149.60*10**9                  
G = 6.67428*10**-11   
n = 10**6             
dt = 400                

#Calculation of gravitational force on the bodies  
def grav_force(x1,x2,y1,y2,mass1,mass2):
    a = abs(x2-x1)                     
    b = abs(y2-y1)                     
    r = sqrt((x2-x1)**2 + (y2-y1)**2) 
    F = (G*mass1*mass2)/r**2           
    theta = arctan(float(b)/a)        

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
x3 = zeros(n, float)
y3 = zeros(n, float)

x1[0] = -1.5*AU; y1[0] = 0
x2[0] = 0; y2[0] = 0
x3[0] = 3*AU; y3[0] = 0
 
v_x1 = zeros(n, float)
v_y1 = zeros(n, float)
v_x2 = zeros(n, float)
v_y2 = zeros(n, float)
v_x3 = zeros(n, float)
v_y3 = zeros(n, float)

v_x1[0] = 0; v_y1[0] = -1000
v_x2[0] = 0; v_y2[0] = 30000
v_x3[0] = 0; v_y3[0] = -7500

#Calculations
teller = range(n-1)
for i in teller:

    Fx_1_2,Fx_2_1,Fy_1_2,Fy_2_1 = grav_force(x1[i],x2[i],y1[i],y2[i],m1,m2)
    Fx_2_3,Fx_3_2,Fy_2_3,Fy_3_2 = grav_force(x2[i],x3[i],y2[i],y3[i],m2,m3)
    Fx_1_3,Fx_3_1,Fy_1_3,Fy_3_1 = grav_force(x1[i],x3[i],y1[i],y3[i],m1,m3)

    Fx_1 = Fx_1_2 + Fx_1_3
    Fx_2 = Fx_2_3 + Fx_2_1
    Fx_3 = Fx_3_2 + Fx_3_1
    Fy_1 = Fy_1_2 + Fy_1_3
    Fy_2 = Fy_2_3 + Fy_2_1
    Fy_3 = Fy_3_2 + Fy_3_1

    v_x1[i+1] = v_x1[i] + dt*Fx_1/m1
    v_x2[i+1] = v_x2[i] + dt*Fx_2/m2
    v_x3[i+1] = v_x3[i] + dt*Fx_3/m3
    v_y1[i+1] = v_y1[i] + dt*Fy_1/m1
    v_y2[i+1] = v_y2[i] + dt*Fy_2/m2
    v_y3[i+1] = v_y3[i] + dt*Fy_3/m3
    
    x1[i+1] = x1[i] + dt*v_x1[i+1]
    x2[i+1] = x2[i] + dt*v_x2[i+1]
    x3[i+1] = x3[i] + dt*v_x3[i+1]
    y1[i+1] = y1[i] + dt*v_y1[i+1]
    y2[i+1] = y2[i] + dt*v_y2[i+1]
    y3[i+1] = y3[i] + dt*v_y3[i+1]
    
    t[i+1] = t[i] + dt

plot(x1,y1, x2,y2, x3,y3,
     legend=('Planet','Small star','Large star'),
     title='Plot of orbit to each body',
     xlabel='x-axis [m]', ylabel='y-axis [m]')

raw_input('Press Enter: ')
