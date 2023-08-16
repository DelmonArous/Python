from scitools.std import *

infile = open('lnsum.dat', 'r')

epsilon = []; exact_error = []; n = []

for line in infile:
    if 'epsilon:' in line:
        words = line.split()
        epsilon.append(float(words[1].strip(',')))
        exact_error.append(float(words[4].strip(',').replace('e','E')))
        n.append(float(words[5].strip('n=')))

infile.close()

epsilon = array(epsilon)
exact_error = array(exact_error)
n = array(n)

plot(n, epsilon, n, exact_error, log='y', legend=('epsilon','exact error'),
     title='Plot of output from file: lnsum.dat')

'''
Unix> python lnsum.py > lnsum.dat  # Redirect the output to a text-file named
                                   # lnsum.dat
'''

        
        
