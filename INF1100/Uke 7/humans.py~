humans = {}
infile = open('human_evolution.txt', 'r')

for line in infile:
    if 'H.' in line:
        name = line[0:21].strip().replace('H.', 'homo')
        when = line[22:36].strip()
        height = line[38:47].strip()
        mass = line[51:60].strip().replace(" ", "")
        brain = line[63:].strip()
        humans[name] = {'height': height, 'mass': mass,
                        'when': when, 'brain': brain}

print humans['homo neanderthalensis']['mass']

#for name in humans:
 # print '%-21s%-16s%-13s%-12s%-s' % \
  #  (name,humans[name]['when'],humans[name]['height'],humans[name]['mass'],humans[name]['brain'])


        
