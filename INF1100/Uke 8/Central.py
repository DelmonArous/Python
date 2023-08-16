from math import *

class Central:
    def __init__(self, f, h=1E-9):
        self.f = f
        self.h = float(h)
    
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h)-f(x-h))/(2*h)

def f1(x):
    return 0.25*x**4
df1 = Central(f1)

for x in [1, 5, 10]:
    df1_value = df1(x)
    exact1 = x**3
    print "f'(%d) = %g   (error:%.2E)" % (x, df1_value, abs(exact1-df1_value))

print '--------------------'

h_values = [0.5, 0.1, 1E-3, 1E-5, 1E-7, 1E-9, 1E-11]

def f2(x):
    return log(x)

for h in h_values:
    df2 = Central(f2, h)
    df2_value = df2(x=10)
    exact2 = (1./x)
    print "f'(%d) = %g   (error:%.2E)" % (x, df2_value, abs(exact2-df2_value))
    

