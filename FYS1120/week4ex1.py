# point_charge.py - Iterative solution of 2D Poisson equation
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# System size and resolution
L = 2.0
N = 21
h = L/(N-1)

# Make the charge density matrix
q = 3.0
rho0 = q/h**2
rho = np.zeros((N,N))
rho[N/2,N/2] = rho0 # Intentional integer division

# Make the initial guess for solution matrix
V = np.zeros((N,N))

# Solver
iterations = 0
eps = 1e-8 # Convergence threshold
error = 2*eps # Dummy error to enter the first loop
while iterations < 1e4 and error > eps:
    V_temp = np.copy(V)
    error = 0.0 # We make this accumulate in the loop
    for j in range(1,N-1): # Avoid updating the boundaries
        for i in range(1,N-1):
            V[i,j] = 0.25*(V_temp[i+1,j] + V_temp[i-1,j] +
                    V_temp[i,j-1] + V_temp[i,j+1] + rho[i,j]*h**2)
            error += abs(V[i,j]-V_temp[i,j])
    iterations += 1
    error /= float(N**2)
print "iterations =",iterations

# Define arrays used for plotting
x = np.linspace(0,L,N)
y = np.linspace(0,L,N)
# meshgrid() by default orders the arrays differently from what
# I prefer. This way, (X[i,j],Y[i,j]) equals (x[i],y[j])
Y,X = np.meshgrid(y,x)

# Plot the potential V
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
CS = plt.contour(X,Y,V,30) # Make a contour plot
#plt.clabel(CS, inline=1, fontsize=10) # Contour labels
plt.title('Point charge in the cavity of a grounded box')
CB = plt.colorbar(CS, shrink=0.8, extend='both')
plt.show()

# Plot the electric field.
Ex,Ey = np.gradient(-V)
Ex /= h
Ey /= h
plt.quiver(X,Y,Ex,Ey)
plt.show()

# Verify that Gauss' law holds
flux =  sum(Ex[N-1,:]) - sum(Ex[0,:]) + sum(Ey[:,N-1]) - sum(Ey[:,0])
flux *= h
print "q =",q,", flux =",flux
