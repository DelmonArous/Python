from scitools.std import *

def S(x, n):
    
    en_prev = 0.    # the previous sum of the Taylor-polynomial 
    an_prev = 1.    # a[0], Taylor-polynomial of degree 0

    for n in range(1,n+1):      # have already calculated for n=0, therefor n=1,2,...,n
        en = en_prev + an_prev  # the current sum of the Taylor-polynomial
        an = (-x**2)/float((2*n-1)*(2*n))*an_prev # a[n], term of Taylor-polynomial of degree n

        # keep giving the previous sum and term new values to compute the Taylor-polynomial
        en_prev = en
        an_prev = an  
        
    return en, an

x = linspace(-4*pi,4*pi,1000)  
y_exact = cos(x)
n_values = range(2,11)    # compute Taylor-polynomial for different degrees (e.g. different n-values),  
                          # the for-loop in the function S(x,n) does not "initiate" until n=2

plot(x, y_exact, 
     axis=[-4*pi,4*pi,-4,4],xlabel='x',ylabel='f(x)',
     title='Plot of Taylor series of cosine', 
     legend='cos(x)')

hold('on')

for n in n_values: 
    y_approx, neglected_term = S(x,n)
    plot(x, y_approx, legend=('n=%g' % (2*n)))

'''
Plot cos(x) and the Taylor series of the function 
to check if the function S(x,n) works correctly. Doing so by
chosing x-values from -4*pi to 4*pi and see how well the difference equations
of different Talylor degrees corespond to cos(x) (e.g. n=0,...,k)
'''

