from math import *

def egg(M, To=20, Ty=70):

    rho = 1.038         # density
    c = 3.7             # specific heat
    K = 5.4*10**(-3)    # thermal conductivity
    Tw = 100            # water temperature
    
    t = M**(2.0/3)*c*rho**(1.0/3)/(K*pi**(2)*(4*pi/3)**(2.0/3))*\
        log(0.76*(To - Tw)/(Ty - Tw))

    print '%.1f min' % (t/60)
    
    return t/60.

for Ty in [63,70]:
    for M in [47,67]:
        for To in [4,25]:
            t = egg(M, To, Ty)
            print 'M=%5.1f To=%5.1f Ty=%5.1f : %3.1f' % (M,To,Ty,t)
            
