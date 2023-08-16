from enthought.mayavi.mlab import *
from numpy import *

R = 50.
Q = 10.
eps0 = 8.854187818*10**-12
x,y,z = mgrid[-100:101:5, -100:101:5, -100:101:5]
r = sqrt(x**2 + y**2 + z**2)
V = 0*x

for i in range(len(r)):
    for j in range(len(r)):
        for k in range(len(r)):
            if R > r[i][j][k]:
            	V[i][j][k] = (Q/(8*pi*eps0*R))*(3-(r[i][j][k]/R)**2)
            else:
                V[i][j][k] = Q/(4*pi*eps0*r[i][j][k])

E = negative(gradient(V))

contour3d(x, y, z, V, contours=20, opacity=0.5)
quiver3d(x[::5], y[::5], z[::5], E[0][::5],E[1][::5],E[2][::5],opacity=0.5)

raw_input('Enter')
