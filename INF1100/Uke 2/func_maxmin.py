from math import *
from scitools.StringFunction import StringFunction
import sys

def maxmin(a, b, n=1000):

    formula = sys.argv[1]
    f = StringFunction(formula)  
    dx = (b - a) / float(n)
    x_list = [a + i*dx for i in range(n+1)]
    y = [f(x) for x in x_list]

    return max(y),min(y)

print maxmin(-pi/2, 2*pi)
