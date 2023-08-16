from math import *

def f(x):
    return exp(x)

a = 1
diff_exact = 2.7182818284590452354
h = 10**(-3)

while h > 10**(-20):
    diff_approx = (f(a-h)-2*f(a)+f(a+h))/float(h**2)
    error = abs(diff_exact-diff_approx)  
    print 'h = %g, diff approx: %g, error: %g' % (h,diff_approx, error)
    h *= 10**(-1)

    
