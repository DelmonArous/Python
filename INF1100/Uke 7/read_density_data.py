from scitools.std import *

try:
    filename = sys.argv[1]
except IndexError:
    print 'Error, provide filename'
    sys.exit(1)

infile = open(filename, 'r')

temp = density = []

for line in infile:
    if '#' not in line:
        words = line.split()
        if len(words) > 1:
            temp.append(float(words[0]))
            density.append(float(words[1]))

infile.close()

temp = array(temp)
density = array(density)

plot(temp, density, 'ro')
