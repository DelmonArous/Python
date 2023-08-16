def read_densities_1(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substance = ' '.join(words[:-1])
    
        densities[substance] = density
        
    infile.close()
    
    return densities

def read_densities_2(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        substance = line[:12].strip()
        density = float(line[12:])
      
        densities[substance] = density

    infile.close()

    return densities

densities2 = read_densities_2('densities.dat')
densities1 = read_densities_1('densities.dat')

if densities1==densities2:
    print 'The dictionaries are the same'
else:
    print 'They do not correspond'

'''
Unix> python density_improved.py
The dictionaries are the same
'''
