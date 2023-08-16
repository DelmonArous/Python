from math import *

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        s = 0.0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

def Taylor_coeff(N):
    '''This function computes the coefficients 
       in each term of the Taylor polynomial of degree N'''
    coeff = [1/float(factorial(k)) for k in range(N+1)]
    return coeff

x = 2
N_values = [5, 25, 50, 100]

# Gives a list of N coefficients to the class Polynomial to compute
# the value of the Taylor polynomial of degree N for value x.
# Comparison between the value of the Taylor polynomial of degree N and
# the exact value.
for N in N_values:
    p = Polynomial(Taylor_coeff(N)) 
    p_value = p(x)
    exact_value = exp(x)
    print 'N=%d: p(%d) = %.16f, exact value = %g, (error=%.2E)' % \
        (N, x, p_value, exact_value, abs(exact_value-p_value))

'''
Unix> python Polynomial_exp.py
N=5: p(2) = 7.2666666666666666 , exact value = 7.38906, (error=1.22E-01)
N=25: p(2) = 7.3890560989306486 , exact value = 7.38906, (error=1.78E-15)
N=50: p(2) = 7.3890560989306486 , exact value = 7.38906, (error=1.78E-15)
N=100: p(2) = 7.3890560989306486 , exact value = 7.38906, (error=1.78E-15)
'''
