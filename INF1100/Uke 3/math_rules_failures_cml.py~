import random, sys
from math import *
      
def equal(expr1, expr2, A=-100, B=100, n=500):
    x = 0
    counter = 0
    while x <= n:
        a = random.uniform(A,B)
        b = random.uniform(A,B)
        x += 1
        if not eval(expr1) == eval(expr2):
            counter += 1
    
    print 'Number of failures: %g \nPercentage of failures: %g %%' % \
        (counter, counter/float(n)*100)
    
    return counter, counter/n*100

try:
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
except IndexError:
    print 'You failed to provide command-line argument(s)!'
    sys.exit(1)
except ValueError:
    print 'The command-line argument(s) do not fit the function!'
    sys.exit(1)

equal(expr1, expr2)
