def C(F):
    C = (5.0/9)*(F - 32)
    print '%.1f degrees equals %d fahrenheit' % (C,F)
    return C
    
def F(C):
    F = ((9.0*C)/5) + 32
    print '%d fahrenheit equals %.1f degrees' % (F,C)
    
    return F
