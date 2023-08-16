from scitools.std import *

# Constants
M = 1.
r0 = 20*M
theta = 167*(pi/180)
v_shell = 0.993
gamma_shell = 1./sqrt(1-v_shell**2)                         
Em = sqrt(1- (2*M/r0) )*gamma_shell    # the relativistic energy per mass 
Lm = r0*gamma_shell*v_shell*sin(theta) # and the angular momentum per mass
                                       # is conserved
dtau = 0.01 # proper time step
N = 1000    # number of time steps


# Defining arrays with given inital conditions
r = zeros(N)
phi = zeros(N)

r[0] = r0
phi[0] = 0

# Calculating the orbit of the rocket
for i in range(N):
    if r[i]/M <= 2: # if we are located inside the black hole,
        N = i       # terminate loop
        break
    else:
        # Calculating very small changes in r- and phi-position 
        r_delta = -sqrt( (Em)**2 - ( 1 + (Lm/r[i])**2 )\
                              *(1- (2*M/r[i])))*dtau
        phi_delta = (Lm/(r[i]**2))*dtau

        # Updating our arrays with new position
        r[i+1] = r[i] + r_delta
        phi[i+1] = phi[i] + phi_delta


# Making the Schwarzerschild radius with r=2M 
t = linspace(0,2*pi,100)
x_schwarz = 2*cos(t)
y_schwarz = 2*sin(t)

# Converting from polar to cartesian coordinates
x = r*cos(phi)
y = r*sin(phi)

# Plot of the trajectory and Schwarzerchild radius
plot(x_schwarz, y_schwarz, '--' , x[:N], y[:N],
     xlabel='x-axis [M]',ylabel='y-axis [M]',
     legend=('Schwarzerschild radius', 'Trajectory of rocket'),
     title='Trajectory of the rocket')

raw_input('Press "Enter": ')

finalphi = max(phi)*(180./pi)
print """\
The spaceship did revolve %g degrees
around the black hole before entering the horizon""" % finalphi

'''
Unix> python oblig9.py 
The spaceship did revolve 196.876 degrees
around the black hole before entering the horizon
'''
