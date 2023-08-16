from scitools.std import *

def fortune(I=2,F=50000,p=6,q=60,N=20):   # Alternative values for arguments
    
    x = zeros(N+1)
    c = zeros(N+1)   # Two arrays created with value 0 in each index
                                # Needed to store values and to plot
    x[0] = F
    c[0] = ((p*q)/10.**4)*F

    for n in range(1, N+1):          # x[n] and c[n] for n=1,2,3,...,N
        x[n] = x[n-1] + (p/100.)*x[n-1] - c[n-1]
        c[n] = c[n-1] + (I/100.)*c[n-1]
    
    return x, c

xn, cn = fortune()

plot(range(len(xn)), xn, 
     xlabel='years',ylabel='amount',
     title='Making a living from a fortune')


