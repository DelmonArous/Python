from scitools.StringFunction import StringFunction
from numpy import linspace
import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])
    f = sys.argv[4]
    filename = sys.argv[5]
except IndexError:
    print 'You have failed to provide command-line arguments!'
    sys.exit(1)

outfile = open(filename, 'w')
formula = StringFunction(f)
x = linspace(a, b, n+1)
data = [x, formula(x)]

outfile.write('   x        f(x)' '\n') # Headline

for i in range(len(x)):
    outfile.write('%5.4f %10.4f' % (data[0][i],data[1][i])) # printing out 
    outfile.write('\n')                                     # the table
outfile.close()

'''
Unix> python write_cml_function.py 0 10 10 'x**2+2*x+1' 'tmp.dat'
--------------------------------------------------------------
### tmp.dat ###
   x        f(x)
0.0000     1.0000
1.0000     4.0000
2.0000     9.0000
3.0000    16.0000
4.0000    25.0000
5.0000    36.0000
6.0000    49.0000
7.0000    64.0000
8.0000    81.0000
9.0000   100.0000
10.0000   121.0000
'''
