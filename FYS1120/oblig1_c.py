from numpy import *
import matplotlib.pyplot as plt

# System size and resolution
a = 2.
b = 3.
V0 = 5.
Nx = 21       # resolution along x-axis inside the box
Ny = 31       # resolution along y-axis inside the box
hx = a/(Nx-1) # steplength along x-axis 
hy = b/(Ny-1) # steplength along y-axis
alpha = a/2.
betha = b/2.

def V_analytic(x,y):
    return (V0/sinh((b/a)*pi))*sin((x/a)*pi)*sinh((y/a)*pi)

# Making the initial guess for solution matrix
# with given conditions
V = zeros((Nx,Ny)) # the resolution of the box
for x in range(Nx):
    V[x,Ny-1] = V0*sin((x/float(Nx))*pi)

# Solver
iterations = 0
eps = 1e-8 # our threshold
error = 2*eps
while iterations < 1e4 and error > eps:
    V_temp = copy(V)
    error = 0.0
    for i in range(1,Nx-1):     # avoid updating the boundaries
        for j in range(1,Ny-1): # because of conditions
            V[i,j]=0.25*(V_temp[i+1,j]+V_temp[i-1,j]+\
                             V_temp[i,j-1]+V_temp[i,j+1])
            error += abs(V[i,j] - V_temp[i,j]) # error between  				     # new generation and old generation 
    iterations += 1                             
    error /= float(Nx*Ny) # mean error in a point
print "iterations = ", iterations

# Defining arrays for plotting
x = linspace(0,a,Nx)
y = linspace(0,b,Ny)
V_alpha = V_analytic(alpha,y) 
V_betha = V_analytic(x,betha)

Y,X = meshgrid(y,x)

plt.plot(y,V_alpha,'-', y, V[10,:], 'o')
plt.legend(('Analytical','Numerical'))
plt.xlabel('y')
plt.ylabel('V(alpha,y)')
plt.title('Comparison between analytical and numerical V(alpha,y)')
plt.figure()

plt.plot(x,V_betha,'-', x, V[:,15], 'o')
plt.legend(('Analytical','Numerical'))
plt.xlabel('x')
plt.ylabel('V(x,betha)')
plt.title('Comparison between analytical and numerical V(x,betha)')
plt.figure()

# Plot the eletric potential V
CS = plt.contour(X,Y,V,30) # Make a contour plot
plt.title('Plot of the numerical electric potential V(x,y)'\
              ' and of the electric field E(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(CS, shrink=0.8, extend='both')

# Defining the electric field E
Ex,Ey = gradient(-V)
Ex /= hx
Ey /= hy
plt.quiver(X,Y,Ex,Ey) # Make a quiver plot of E
plt.show()
